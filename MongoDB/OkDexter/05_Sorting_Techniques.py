from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['OkDexter']
col = db['Dexter-Collection']

# sorting data in alphabetical prder
mydoc = col.find().sort('name', 1)  # Ascending
# mydoc = col.find().sort('name', -1)  # Descending
for x in mydoc:
    print(x)
