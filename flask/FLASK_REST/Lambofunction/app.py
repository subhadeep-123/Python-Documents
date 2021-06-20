import os
from flask import Flask
from datetime import datetime
from pytz import all_timezones, timezone as tz
from flask_restful import Api, Resource, reqparse

# Local Import
from config import Config


app = Flask(__name__)
app.config.from_object(os.getenv('Environment_Config'))
api = Api(app)


class All_Timezones(Resource):
    def get(self):
        timezones = []
        for tzone in all_timezones:
            try:
                timezones.append(tzone.split('/')[-1].title())
            except IndexError:
                timezones.append(tzone.title())
        return {"timezones": timezones}

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass


class Time_By_Timezone(Resource):
    def __init__(self):
        self.parser = self.setupParser()
        self.args = self.parser.parse_args()
        self.server_time = tz(Config.SERVER_TIME_ZONE).localize(datetime.now())
        super(Time_By_Timezone, self).__init__()

    @staticmethod
    def setupParser():
        parser = reqparse.RequestParser()
        parser.add_argument('format', type=str,
                            location='args', required=False)
        return parser

    def get(self, timezone):
        format = self.args.get('format', None)
        if format is None:
            format = Config.DEFAULT_DATETIME_FORMAT

        for _timezone in all_timezones:
            if timezone.lower() in _timezone.lower():
                try:
                    continent = _timezone.split("/")[0].title()
                except IndexError:
                    continent = None
                timezone = timezone.replace("_", " ").title()
                client_tz = tz(_timezone)
                client_dt = self.server_time.astimezone(client_tz)
                client_dt = client_dt.strftime(format)
                return {"continent": continent,
                        "timezone": timezone,
                        "datetime": client_dt,
                        "format": format
                        }
        else:
            return {"error": "Timezone not found"}, 404

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass


if __name__ == '__main__':
    api.add_resource(All_Timezones,
                     '/api/v1.0/timezones',
                     '/get_all_timezones')
    api.add_resource(Time_By_Timezone,
                     '/api/v1.0/time_by_timezone/<string:timezone>',
                     endpoint="get_time_by_timezone")

    app.run()
