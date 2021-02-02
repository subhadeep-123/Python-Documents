from pymongo import MongoClient
import re
import os
os.system('cls')
client = MongoClient('localhost', 27017)
db = client['OkDexter']
col = db['Dexter-Collection']

query = {"name": "Richard"}  # Normal Query
query = {"name": {"$regex": "^S"}}  # query search using regex

mydoc = col.find(query)
for x in mydoc:
    print(x)
