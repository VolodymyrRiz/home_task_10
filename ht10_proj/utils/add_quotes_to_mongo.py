import json
from bson.objectid import ObjectId
from pymongo import MongoClient

client = MongoClient('mongodb+srv://vvrizun:rizun2024@cluster0.klgot1w.mongodb.net/hw?retryWrites=true&w=majority&appName=Cluster0')
db = client

with open('quotes.json', 'r', encoding='utf-8') as fd:
    quotes = json.load(fd)
    
for quote in quotes:
    author = db.authors.get({'fullname': quote['author']})    
    if author:
        db.quotes({
            'quote': quote['quote'],
            'tags': quote['tags'],
            'author': ObjectId(author['_id'])
        })