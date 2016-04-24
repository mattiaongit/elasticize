Elasticize
==========

Elasticize is a simple way to transfer data from MongoDB to Elasticsearch.



Setup
-----
Use the config.json file to specify the source and destination of your data

```json
{
	"MONGO_DATABASE": "source_mongo_db",
	"MONGO_COLLECTION": "source_mongo_collection",
	"ES_URL": "http://localhost:9200",
	"ES_INDEX": "destination_index",
	"ES_TYPE" : "destination_type"
}
```

Run
---
Once the configuration is done, just run:

```python
python elasticize.py
```

Dependencies
------------

Elasticize is written in Python, so you'll need to have python installed.
Other few dependecis are needed as **Requests**, an http request python library to send request to ES and **Pymongo** to fetch data from a MongoDB database.

Here's a list of the dependecies needed:

- [Python](https://www.python.org/downloads/) 2.x
- [Requests](http://docs.python-requests.org/en/master/user/install/#install)
- [Pymongo](https://api.mongodb.org/python/current/installation.html)
