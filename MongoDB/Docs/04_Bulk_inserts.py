import pymongo
import datetime

client = pymongo.MongoClient('localhost', 27017)

db = client['Some_Database']
collection = db['Some_Collection']

new_post = [
    {
        "author": "Subhadeep Banerjee",
        "text": "Another Post",
        "tags": ["bulk", "insert"],
        "date": datetime.datetime(2009, 11, 12, 11, 14)
    },
    {
        "author": "Ria Gupta",
        "title": "MongoDB is fun",
        "text": "And Pretty easy too!!",
        "date": datetime.datetime(2009, 11, 10, 10, 45)
    },
    {
        "author": "Shreya Mukherjee",
        "title": "MongoDB is fun",
        "text": "And Pretty easy too!!",
        "date": datetime.datetime(2009, 11, 10, 10, 45)
    },
    {
        "author": "Litisha Mohapatro",
        "title": "MongoDB is fun",
        "text": "And Pretty easy too!!",
        "date": datetime.datetime(2009, 11, 10, 10, 45)
    },
    {
        "author": "Satej Manna",
        "title": "MongoDB is fun",
        "text": "And Pretty easy too!!",
        "date": datetime.datetime(2009, 11, 10, 10, 45)
    },
    {
        "author": "Souma Mitra",
        "title": "MongoDB is fun",
        "text": "And Pretty easy too!!",
        "date": datetime.datetime(2009, 11, 10, 10, 45)
    },
    {
        "author": "Shubham Nag",
        "title": "MongoDB is fun",
        "text": "And Pretty easy too!!",
        "date": datetime.datetime(2009, 11, 10, 10, 45)
    },
    {
        "author": "Suvhradip Ghosh",
        "title": "MongoDB is fun",
        "text": "And Pretty easy too!!",
        "date": datetime.datetime(2009, 11, 10, 10, 45)
    },
    {
        "author": "Rajarshee Bhadra",
        "title": "MongoDB is fun",
        "text": "And Pretty easy too!!",
        "date": datetime.datetime(2009, 11, 10, 10, 45)
    },
    {
        "author": "Argha Chatterjee",
        "title": "MongoDB is fun",
        "text": "And Pretty easy too!!",
        "date": datetime.datetime(2009, 11, 10, 10, 45)
    }
]
posts = collection.posts
# posts = db.posts
result = posts.insert_many(new_post)
result.inserted_ids
