from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello Workd"


@app.route('/second')
def hi():
    return "Hey Whats Up"


if __name__ == '__main__':
    app.run(debug=True)
