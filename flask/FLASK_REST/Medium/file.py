import json
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
app.config['DEBUG'] = True
api = Api(app)

# dummy data for end points
input = open('./json/data.json')
data = json.load(input)
hospital = data['hospital']
services = data['services']
complaint = data['complaint']


class Services(Resource):
    def get(self):
        return {"services": services}


class Complaints(Resource):
    def get(self):
        return {"complaints": complaint}

    def post(self):
        print(request)
        complaint.append({
            "name": request.json['name'],
            "email": request.json['email'],
            "contact": request.json['contact'],
            "description": request.json['description']
        })
        with open('./json/data.json', 'w') as data_file:
            data['complaint'] = complaint
            json.dump(data, data_file)

        return {'status': 'success'}


class Hospital(Resource):
    def get(self):
        return {"hospitals": hospital}

    def post(self):
        hospital.append({
            "name": request.json['name'],
            "cleṇanliness": request.json['cleanliness'],
            "facilities": request.json["facilities"],
            "doc-behaviour": request.json['doc-behaviour'],
            "quality-of-service": request.json['quality-of-service']
        })

        with open('./json/data.json', 'w') as data_file:
            data['hospital'] = hospital
            json.dump(data, data_file)

        return {'status': 'success'}


api.add_resource(Services, '/services')
api.add_resource(Complaints, '/complaints')
api.add_resource(Hospital, '/hospital')

if __name__ == '__main__':
    app.run()
