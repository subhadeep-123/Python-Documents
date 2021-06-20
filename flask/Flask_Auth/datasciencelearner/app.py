import pymongo
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

# connecting to the mongoserver
client = pymongo.MongoClient()
db = client['app_database']
col = db['User']


app = Flask(__name__)
app.config['DEBUG'] = True
jwt = JWTManager(app)

# JWT Config
app.config["JWT_SECRET_KEY"] = b'\x04\xf9;\xf37\x084\r\xc9\x7fzY\xfd\x81:\xee'


# Registration endpoint
@app.route("/register", methods=["POST"])
def register():
    email = request.form["email"]
    if email is None:
        app.logger.error("Email Id Missing")
    # Checking if the user is in the database
    test = col.find_one({"email": email})
    if test:
        return jsonify(message="User Already Exists"), 409
    else:
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        password = request.form["password"]
        user_info = dict(first_name=first_name,
                         last_name=last_name,
                         email=email,
                         password=password)
        inserted_id = col.insert_one(user_info).inserted_id
        app.logger.info(f"Data Inserted - {inserted_id}")

        return jsonify(message="User added Sucessfully"), 201


# Login endpoint
@app.route("/login", methods=["POST"])
def login():
    if request.is_json:
        email = request.json["email"]
        password = request.json["password"]
    else:
        email = request.form["email"]
        password = request.form["password"]

    test = col.find_one(
        {"email": email,
         "password": password}
    )
    if test:
        access_token = create_access_token(identity=email)
        return jsonify(message="Login Succeeded!",
                       access_token=access_token), 201
    else:
        app.logger.error('Credentials Already Exists')
        return jsonify(message="Bad Email or Password"), 401


# Secured Test route
@jwt_required
@app.route("/dashboard")
def dashboard():
    return jsonify(message="Welcome! to the Data Science Learner")


# Custom error handler
@app.errorhandler(404)
def noData(error):
    return "No Data to show here.", error


# Check Method to show all the data
@app.route('/alldata', methods=['GET'])
def allData():
    dataList = list()
    if request.method == 'GET':
        for i in col.find({}):
            i.pop('_id')
            dataList.append(i)
        if len(dataList) == 0:
            return noData(404)
        else:
            return jsonify(dataList)


if __name__ == '__main__':
    app.run()
