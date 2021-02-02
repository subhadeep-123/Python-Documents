import pymongo
client = pymongo.MongoClient('localhost', 27017)
print(client.list_database_names())
# We can not create DB until we provide some data with it
