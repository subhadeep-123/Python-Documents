import sqlite3 as sql
from flask import Flask, render_template, request

# conn = sql.connect('database.db')
# print("Opened database successfully")

app = Flask(__name__)
app.config['DEBUG'] = True

# conn.execute(
#     'CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
# print("Table created successfully")


@app.route('/new')
def new_student():
    return render_template('student.html')


@app.route('/addrec', methods=['GET', 'POST'])
def addrec():
    if request.method == 'POST':
        conn = sql.connect('database.db')
        try:
            nm = request.form['nm']
            addr = request.form['add']
            city = request.form['city']
            pin = request.form['pin']

            cur = conn.cursor()
            cur.execute(
                'INSERT INTO students (name, addr, city, pin) VALUES (?, ?, ?, ?)', (nm, addr, city, pin))
            conn.commit()
            msg = "Record successfully added."
        except:
            conn.rollback()
            msg = "Error in insert operation"

        finally:
            return render_template('results.html', msg=msg)


@app.route('/list')
def list():
    conn = sql.connect('database.db')
    conn.row_factory = sql.Row

    cur = conn.cursor()
    cur.execute("SELECT * FROM students")

    rows = cur.fetchall()
    return render_template('list.html', rows=rows)


@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run()
