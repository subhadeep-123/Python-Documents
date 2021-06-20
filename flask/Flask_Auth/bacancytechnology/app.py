import jwt
import uuid
import datetime
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request, make_response
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = '004f2af45d3a4e161a7dd2d17fdae47f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookstore.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


# Making database models
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.Integer)
    name = db.Column(db.String(50))
    password = db.Column(db.String(50))
    admin = db.Column(db.Boolean)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(50), unique=True, nullable=False)
    Author = db.Column(db.String(50), unique=True, nullable=False)
    Publisher = db.Column(db.String(50), nullable=False)
    book_prize = db.Column(db.Integer)


def token_required(f):
    """
    This function will create a custom decorator 
    with the code required to create and validate 
    tokens.
    """
    @wraps
    def decorator(*args, **kwargs):
        token = None
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return jsonify(
                {
                    'message': 'A valid Token is missing'
                }
            )

        try:
            data = jwt.decode(
                token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = Users.query.filter_bu(
                public_id=data['public_id']).first()
        except Exception as err:
            return jsonify(
                {
                    'message': 'Token is Invalid'
                }
            )
        return f(current_user, *args, **kwargs)
    return decorator


@app.route('/register', methods=['POST'])
def signup_user():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')

    new_user = Users(
        public_id=str(uuid.uuid4()),
        name=data['name'],
        password=hashed_password,
        admin=False
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify(
        {
            'message': 'User  Registered Successfully'
        }
    )


@app.route('/login', methods=['POST'])
def login_user():
    """
    With the login route, we will create a view to handle 
    the user login feature. When a user logs in, the 
    entered password is matched with the user’s stored 
    password. If the password matches successfully, a 
    random token is generated to access the Bookstore API.
    """
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return make_response(
            'Could not verify', 401,
            {
                'Authentication': 'Login Required'
            }
        )
    user = Users.query.filter_by(name=auth.username).first()
    if check_password_hash(user.password, auth.password):
        token = jwt.encode(
            {
                'public_id': user.public_id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=45)
            },
            app.config['SECRET_KEY'],
            "HS256"
        )
        return jsonify(
            {
                'token': token
            }
        )
    return make_response(
        'could not verify',  401,
        {
            'Authentication': '"login required"'
        }
    )


@app.route('/users', methods=['GET'])
def get_all_users():
    """
    route in the app.py file to get all the 
    registered users.
    """
    users = Users.query.all()
    result = []
    for user in users:
        user_data = {}
        user_data['public_id'] = user.public_id
        user_data['name'] = user.name
        user_data['password'] = user.password
        user_data['admin'] = user.admin
        result.append(user_data)
    return jsonify(
        {'users': result}
    )


@app.route('/book', methods=['POST'])
@token_required
def create_book(current_user):
    """
     a route for all the registered users to 
     create a new book. The following code 
     creates a route to meet this requirement.
    """
    data = request.get_json()
    new_books = Books(
        name=data['name'],
        Author=data['Author'],
        Publisher=data['Publisher'],
        book_prize=data['book_prize'],
        user_id=current_user.id
    )
    db.session.add(new_books)
    db.session.commit()
    return jsonify(
        {'message': 'New Book entry Created'}
    )


@app.route('/books', methods=['GET'])
@token_required
def get_books(current_user):
    """
    A route to allow a logged in user with valid 
    token to get all the books in the Books table.
    """
    books = Books.query.filter_by(user_id=current_user.id).all()
    output = []
    for book in books:
        book_data = {}
        book_data['id'] = book.id
        book_data['name'] = book.name
        book_data['Author'] = book.Author
        book_data['Publisher'] = book.Publisher
        book_data['book_prize'] = book.book_prize
        output.append(book_data)
    return jsonify(
        {
            'list_of_books': output
        }
    )


@app.route('/books/<book_id>', methods=['DELETE'])
@token_required
def delete_book(current_user, book_id):
    """
    last route to delete a specific book. We will create
    a view responsible for handling requests made to delete
    an existing record in the Books table.
    """
    book = Books.query.filter_by(id=book_id, user_id=current_user.id).first()
    if not book:
        return jsonify({'message': 'book does not exist'})

    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted'})


if __name__ == '__main__':
    app.run()
