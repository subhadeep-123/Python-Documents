from flask import Flask, request
from flask.helpers import make_response
from markupsafe import escape

app = Flask(__name__)


# Reading Cookies
@app.route('/')
def index():
    username = request.cookies.get('username')
    return f"{escape(username)}"


# # Storing Cookies
app.route('/two')


def index2():
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the_username')
    return resp


if __name__ == '__main__':
    app.run(debug=True)
