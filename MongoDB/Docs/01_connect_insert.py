from pymongo import MongoClient
import datetime
# client = MongoClient()  # This will take the default host and port

# This is to send the default host and port specifically
client = MongoClient()

db = client['test-database']  # Creating an instance of db with db name

post = {
    "author": "Mike",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.utcnow()
}
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)
