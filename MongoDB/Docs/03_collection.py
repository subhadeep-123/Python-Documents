from pymongo import MongoClient
import datetime
from pprint import pprint

client = MongoClient('localhost', 27017)
db = client['test-collection']
