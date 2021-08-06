import csv
from pymongo import MongoClient
import datetime

client = MongoClient('localhost', 27017)
db = client.test
collection = db.flows
sp = []

with open('flow.csv', 'r') as csvfile:
    for line in csvfile:
        FlowArray = []
        sp = line.split(',')
        d = datetime.datetime.strptime(str(sp[9]), "%Y-%m-%dT%H:%M:%S.000Z\n")
        for i in range(7):
            if sp[i+1] is not "":
                FlowArray.append(sp[i+1])

        collection.insert_one({"id": sp[0], "Flow" : FlowArray, "gender" : sp[8], "TimeStamp" : d})
