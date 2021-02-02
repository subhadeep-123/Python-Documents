import pymongo
from pprint import pprint
client = pymongo.MongoClient()
db = client['test-database']

# Printing the data that is in the database
pprint(db.posts.find_one())

# Print the data that is not present in the database
pprint(db.posts.find_one({'author': "Elliot"}))
