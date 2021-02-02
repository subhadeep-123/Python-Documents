from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['OkDexter']
col = db['Dexter-Collection']

x = col.find_one()  # for finding single occurences in collection/table
print(x)
print(col.find())  # For finding all occurences in collection
