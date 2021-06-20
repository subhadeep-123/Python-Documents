from flask import Flask, render_template, request, redirect, url_for, flash, make_response, session

import datetime

app = Flask(__name__)
app.permanent_session_lifetime = datetime.timedelta(days=365)
app.secret_key = b"c\xd1\x0c\xef\xf3\xafcSI\\\xdcA\xacd\x9b\xb2\x9c\xfaR\xbe\xf5_\xae\x88\xb6C\xfe*4\xac\xb4\x04\x05\xe08k9\xeb\xabG\x82\x97\xa6\xa0~r\'=\xd0\xe6\xbd\x87\x1a7cS\x89-\xf6\xcb\x81\xcc\xd9\x0b^\xa7\xa8I\x13X\xfc\xd0\xf0f:@\xaf\x1a\\97\xcc\x87*z\x96\x040\xa3\xf6\xc1\xf5\xd8\xc5\x8b\xb9;QS\x13\x8bN\xcb\xf4z`;\'\x0cK\xdef\x8b\xa0/Use\xe9\x95IsT\x07\x13"


@app.route('/visits-counter/')
def visits():
    print(session)
    if 'visits' in session:
        # reading and updating session data
        session['visits'] = session.get('visits') + 1
    else:
        session['visits'] = 1  # setting session data
    return "Total visits: {}".format(session.get('visits'))


@app.route('/delete-visits/')
def delete_visits():
    session.pop('visits', None)  # delete visits
    return 'Visits deleted'


@app.route('/session/')
def updating_session():
    res = str(session.items())

    cart_item = {'pineapples': '10', 'apples': '20', 'mangoes': '30'}
    if 'cart_item' in session:
        session['cart_item']['pineapples'] = '100'
        session.modified = True
    else:
        session['cart_item'] = cart_item

    return res


if __name__ == '__main__':
    app.run()
