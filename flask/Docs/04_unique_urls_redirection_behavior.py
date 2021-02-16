from flask import Flask
app = Flask(__name__)


@app.route('/projects/')
def hello():
    return "The Project page"


@app.route('/about')
def hi():
    return "The About Page"


if __name__ == '__main__':
    app.run(debug=True)
