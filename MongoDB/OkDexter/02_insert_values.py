from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['OkDexter']
col = db['Dexter-Collection']

mylist = [
    {
        "id": 1,
        "name":
        "John",
        "address": "Highway 37"
    },
    {
        "id": 2,
        "name": "Peter",
        "address": "Lowstreet 27"
    },
    {
        "id": 3,
        "name": "Amy",
        "address": "Apple st 652"
    },
    {
        "id": 4,
        "name": "Hannah",
        "address": "Mountain 21"
    },
    {
        "id": 5,
        "name": "Michael",
        "address": "Valley 345"
    },
    {
        "id": 6,
        "name": "Sandy",
        "address": "Ocean blvd 2"
    },
    {
        "id": 7,
        "name": "Betty",
        "address": "Green Grass 1"
    },
    {
        "id": 8,
        "name": "Richard",
        "address": "Sky st 331"
    },
    {
        "id": 9,
        "name": "Susan",
        "address": "One way 98"
    },
    {
        "id": 10,
        "name": "Vicky",
        "address": "Yellow Garden 2"
    },
    {
        "id": 11,
        "name": "Ben",
        "address": "Park Lane 38"
    },
    {
        "id": 12,
        "name": "William",
        "address": "Central st 954"
    },
    {
        "id": 13,
        "name": "Chuck",
        "address": "Main Road 989"
    },
    {
        "id": 14,
        "name": "Viola",
        "address": "Sideway 1633"
    }
]

x = col.insert_many(mylist)
dblist = client.list_database_names()
if input('Enter DB - ') in dblist:
    print("The database exists")
else:
    print("Not Present")
print(dblist)

for i in col.find():
    print(i)
