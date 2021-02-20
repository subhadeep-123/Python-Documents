from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/OpenUp"
app.config["MONGO_DBNAME"] = 'records'
mongo = PyMongo(app)
db = mongo.db
col = mongo.db.records


@app.route('/')
def index():
    records = col.find()
    return render_template('index.html', names=records)


if __name__ == '__main__':
    app.run(debug=True)
