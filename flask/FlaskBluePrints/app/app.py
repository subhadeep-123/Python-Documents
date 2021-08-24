from flask_restful import Api
from flask import Flask, Blueprint

# Internal Imports
from api.routes import Foo
from api.routes import Bar
from view.routes import view_routes

app = Flask(__name__)
api_bp = Blueprint('api', __name__)
api = Api(app)


def create_app():

    api.add_resource(Foo, '/foo')
    api.add_resource(Bar, '/bar')

    # Register the blue prints
    app.register_blueprint(api_bp)
    app.register_blueprint(view_routes)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
