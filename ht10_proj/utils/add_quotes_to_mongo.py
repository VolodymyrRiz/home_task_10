import json
from bson.objectid import ObjectId
from pymongo import MongoClient
from pymongo.server_api import ServerApi


client = MongoClient('mongodb+srv://vvrizun:rizun2024@cluster0.klgot1w.mongodb.net/hw?retryWrites=true&w=majority&appName=Cluster0', server_api=ServerApi('1')) 

db = client.hw


with open('quotes.json', 'r', encoding='utf-8') as fd:
    quotes = json.load(fd)
   
    
for quote in quotes:
    
    author = db.authors.find_one({'fullname': quote['author']})    
    print(author)
    if author:
        db.quotes.insert_one({
            'quote': quote['quote'],
            'tags': quote['tags'],
            'author': ObjectId(author['_id'])
        })
        