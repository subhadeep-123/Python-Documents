from flask import Flask, request
from flask.helpers import make_response

app = Flask(__name__)


# Reading Cookies
@app.route('/')
def index():
    username = request.cookies.get('username')


# Storing Cookies
app.route('/two')


def index2():
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the_username')
    return resp
