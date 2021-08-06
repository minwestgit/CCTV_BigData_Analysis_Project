import csv
from pymongo import MongoClient
import datetime

client = MongoClient('localhost', 27017)
db = client.test
collection = db.tests2


with open('test_REALREAL.csv', 'r') as csvfile:
    for line in csvfile:
        sp = line.split(',')
        d = datetime.datetime.strptime(str(sp[2]), "%Y-%m-%dT%H:%M:%S.000Z")
        collection.insert_one({"id": sp[0], "category name" : sp[1], "TimeStamp" : d , "gender" : sp[3]})
