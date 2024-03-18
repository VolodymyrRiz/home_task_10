import json
from bson.objectid import ObjectId
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from models2 import Authors, Quotes
import connect2 as connect2
import os

client = MongoClient('mongodb://localhost') 

db = client.hw


# with open('quotes.json', 'r', encoding='utf-8') as fd:
#     quotes = json.load(fd)
     
# author_1 = Authors.objects()  
# quote_1 = Quotes.objects()   
# for quote in quotes:
    
#     for aut in author_1:
#         if quote['author'] in aut.fullname:
#             print(aut)
#             print(aut.fullname)
#             input()
           
        
#             quot = Quotes(
#                 quote=quote.get['quote'],
#                 tags=quote.get['tags'],
#                 #'author': quote['author'],
#                     #ObjectId(aut['_id'])
#             )
#             quot.save()
#             print(quot)
        
# with open("quotes.json", 'r', encoding="utf-8") as file:
#         data_of_quotes = json.load(file)
#         for quote_ in data_of_quotes:
#             quot = Quotes(author=quote_.get("author"),
#                             quote=quote_.get("quote"),
#                             tags=quote_.get("tags"))
#             quot.save()         




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