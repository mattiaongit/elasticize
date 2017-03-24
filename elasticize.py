import requests
import pymongo
import json
import datetime
from elasticsearch import Elasticsearch
from elasticsearch import helpers
config = json.loads(open('config.json', 'r').read())

connection = pymongo.Connection()
db = connection[config['MONGO_DATABASE']]
es = Elasticsearch(config['ES_URL'])


def outputJSON(obj):
    return obj.strftime('%Y-%m-%dT%H:%M:%S')

collection = db[config['MONGO_COLLECTION']].find({})
documents = []

for n in range(0, collection.count()):
    record = collection.next()
    document = {    "_index": config['ES_INDEX'],
                    "_type": confing['ES_TYPE'],
                    "_id": record.id,
                    "_source": json.dumps(record, default=outputJSON)
                }
    documents.append(document)

helpers.bulk(es,documents, stats_only=True, request_timeout= 320)
