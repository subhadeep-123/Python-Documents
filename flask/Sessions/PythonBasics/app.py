from flask import Flask, session, redirect, request
from flask.helpers import url_for

app = Flask(__name__)
app.secret_key = b"c\xd1\x0c\xef\xf3\xafcSI\\\xdcA\xacd\x9b\xb2\x9c\xfaR\xbe\xf5_\xae\x88\xb6C\xfe*4\xac\xb4\x04\x05\xe08k9\xeb\xabG\x82\x97\xa6\xa0~r\'=\xd0\xe6\xbd\x87\x1a7cS\x89-\xf6\xcb\x81\xcc\xd9\x0b^\xa7\xa8I\x13X\xfc\xd0\xf0f:@\xaf\x1a\\97\xcc\x87*z\x96\x040\xa3\xf6\xc1\xf5\xd8\xc5\x8b\xb9;QS\x13\x8bN\xcb\xf4z`;\'\x0cK\xdef\x8b\xa0/Use\xe9\x95IsT\x07\x13"


@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return f"Logger in as {username}<br> <b><a href = '/logout'>click here to log out</a></b>"
    return "You are not logged in <br><a href = '/login'>" + "click here to log in</a>"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
	
   <form action = "" method = "post">
      <p><input type = text name = username/></p>
      <p<<input type = submit value = Login/></p>
   </form>	
'''


@app.route('/logout')
def logout():
    # remove the username from the session if it is there
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
