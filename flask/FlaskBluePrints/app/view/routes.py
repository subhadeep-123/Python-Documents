from flask import Blueprint

view_routes = Blueprint('view', __name__)


@view_routes.route('/')
def index():
    return "<h1>Welcome to the homepage</h1>"
