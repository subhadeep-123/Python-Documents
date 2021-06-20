from flask import Flask, url_for, redirect, abort

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login')
def login():
    abort(404)


@app.route('/testerror')
@app.errorhandler(401)
def errorPage():
    return "This Page does not exists - 404",


if __name__ == '__main__':
    app.run()
