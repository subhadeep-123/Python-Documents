from flask import Flask, request, redirect
from markupsafe import escape

app = Flask(__name__)


@app.route('/dologin')
def do_the_login():
    return 'Do Login'


@app.route('/<showLogin>')
def show_the_login_form(showLogin):
    return escape(showLogin)


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(do_the_login())
    else:
        return redirect(show_the_login_form('yoyo'))


if __name__ == '__main__':
    app.run(debug=True)
