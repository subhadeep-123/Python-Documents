from flask import Flask, session, redirect, url_for, request
from markupsafe import escape

app = Flask(__name__)

# Need to keep this really really safe
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def index():
    if 'username' in session:
        return f"Logged in as {escape(session['username'])}"
    return 'You are Logged in'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] == request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login?
        </form>
    '''


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))
