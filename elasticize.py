import requests, pymongo, json, datetime
config = json.loads(open('config.json', 'r').read())

document_url = '{0}/{1}/{2}/'.format(config['ES_URL'],config['ES_INDEX'],config['ES_TYPE'])

connection = pymongo.Connection()
db = connection[config['MONGO_DATABASE']]
collection = db[config['MONGO_COLLECTION']].find({}, {'_id': 0})


def outputJSON(obj):
    return obj.strftime('%Y-%m-%dT%H:%M:%S')


for n in range(0, collection.count()):
    document = json.dumps(collection.next(), default=outputJSON)
    requests.post("{0}{1}".format(document_url, n), data=document)
