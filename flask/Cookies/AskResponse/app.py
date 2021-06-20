from flask import Flask, request, make_response
from markupsafe import escape

app = Flask(__name__)


@app.route('/setcookie')
def setcookie():
    resp = make_response("The cookies has been set")
    resp.set_cookie('Name', 'Subhadeep Banerjee')
    return resp


@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('Name', None)
    return escape(f"<h1>Welcome {name}</h1>")


if __name__ == '__main__':
    app.run(debug=True)
