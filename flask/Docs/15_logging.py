from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    app.logger.debug('A value for debugging')
    app.logger.warning('A warning occurred')
    app.logger.error('An error occurrd')
    return "Hello Workd"


if __name__ == '__main__':
    app.run(debug=True)
