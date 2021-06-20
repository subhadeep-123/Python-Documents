from flask import Flask, render_template, request, make_response
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/setcookie', methods=['GET', 'POST'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']
        resp = make_response(render_template('readcookie.html'))
        resp.set_cookie('userID', user)
        return resp


@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID', None)
    return escape(f"<h1>Welcome {name}</h1>")


if __name__ == '__main__':
    app.run(debug=True)
