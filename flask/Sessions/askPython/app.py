from flask import Flask, session

app = Flask(__name__)
app.secret_key = b'$\xa6\x1c\x06\x8b\xa6B\xb3\x13uz\xb9\\\xca+\xcd'


@app.route('/setsession')
def setsession():
    session['Username'] = 'Admin'
    return "The session has been set"


@app.route('/getsession')
def getsession():
    if 'Username' in session:
        Username = session['Username']
        return f"Welcome {Username}"
    else:
        return "Welcome Anonymous"


@app.route('/popsession')
def popsession():
    session.pop('Username', None)
    return "You are logged out"


if __name__ == '__main__':
    app.run(debug=True)
