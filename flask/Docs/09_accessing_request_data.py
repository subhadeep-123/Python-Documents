from flask import Flask, request

app = Flask(__name__)

with app.test_request_context('/hello', method='POST'):
    assert request.path == '/hello'
    assert request.method == 'POST'
