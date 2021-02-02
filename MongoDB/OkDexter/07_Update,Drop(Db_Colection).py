from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['OkDexter']
col = db['Dexter-Collection']


# col.drop()  # drop collection
client.drop_database("OkDexter")  # for droping the db
print(client.list_database_names())


# myquery = {"name": "William"}
# newvalues = {"$set": {"name": "Andrew"}}

# col.update_one(myquery, newvalues)  # update single query/record
# col.update_many(myquery, newvalues)  #updating many records even using regex
# for x in col.find().limit(4):  # limit used for how much data needed to be shown
#     print(x)
