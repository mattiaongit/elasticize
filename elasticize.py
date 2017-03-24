import requests
import pymongo
from pymongo import MongoClient
import json
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch import helpers
config = json.loads(open('config.json', 'r').read())

connection = pymongo.MongoClient()
db = connection[config['MONGO_DATABASE']]
es = Elasticsearch(config['ES_URL'])

def outputJSON(obj):
    if isinstance(obj, datetime):
        return obj.strftime('%Y-%m-%dT%H:%M:%S')

collection = db[config['MONGO_COLLECTION']].find({})
documents = []

print("Creating documents...")
for n in range(0, collection.count()):
    record = collection.next()
    _id = str(record['_id'])
    map(record.pop, ['_id'])
    document = {    "_index": config['ES_INDEX'],
                    "_type": config['ES_TYPE'],
                    "_id": _id,
                    "_source": json.dumps(record, default=outputJSON)
                }
    documents.append(document)

print("{0} documents created, starting bulk inserting...").format(len(documents))
helpers.bulk(es,documents, stats_only=True, request_timeout= 320)
