import pymongo
from pprint import pprint

client = pymongo.MongoClient('localhost', 27017)

db = client['Some_Database']
collection = db['Some_Collection']

# print(collection.posts.estimated_document_count())

# for post in collection.posts.find():
#     pprint(post['author'])
for post in collection.posts.find():
    if post['author'] == "Subhadeep Banerjee":
        print(post["text"])
