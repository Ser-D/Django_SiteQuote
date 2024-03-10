import json
from bson.objectid import ObjectId

from pymongo import MongoClient

uri = "mongodb+srv://userhw8:<PASS>@atlascluster.dkms1wa.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection

db = client.hw9

with open('quotes.json', encoding='utf-8') as fd:
    quotes = json.load(fd)

for quote in quotes:
    author = db.authors.find_one({'fullname': quote['author']})
    if author:
        db.quotes.insert_one({
            'quote': quote['quote'],
            'tags': quote['tags'],
            'author': ObjectId(author['_id'])
        })

