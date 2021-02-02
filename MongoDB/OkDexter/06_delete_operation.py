from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['OkDexter']
col = db['Dexter-Collection']


# query = {"name": {"$regex": "^O"}}
# query = {"name": "Richard"}

# doc = col.delete_manys(query)
for y in col.find():
    print(y)
