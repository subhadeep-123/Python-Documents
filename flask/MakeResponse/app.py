from flask import Flask, make_response, render_template

app = Flask(__name__)


@app.route('/')
def index():
    resp = make_response(render_template('index.html'), 200)
    resp.headers['Temp-X-Test'] = 'This is a test header'
    return resp


app.run()
