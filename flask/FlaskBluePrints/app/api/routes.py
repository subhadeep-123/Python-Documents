from flask_restful import Resource


class Foo(Resource):
    def get(self):
        return "Foo Get"


class Bar(Resource):
    def get(self):
        return "Bar Get"
