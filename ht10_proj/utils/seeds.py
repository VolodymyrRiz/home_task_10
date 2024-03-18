import json
from ht10_proj.quotes.templatetags.models2 import Authors, Quotes
import connect2
from bson.objectid import ObjectId
from pymongo import MongoClient
from pymongo.server_api import ServerApi

author_1 = Authors.objects() 
def load_authors():
    # with open("authors.json", 'r', encoding="utf-8") as file:
    #     data_of_authors = json.load(file)
    #     for author in data_of_authors:
    #         auth = Author(fullname=author.get("fullname"),
    #                      born_date=author.get("born_date"),
    #                      born_location=author.get("born_location"),
    #                      description=author.get("description"))
    #         auth .save()
    with open("quotes.json", 'r', encoding="utf-8") as file:
        data_of_quotes = json.load(file)
        for quote_ in data_of_quotes:
            quot = Quotes(author=author_1.get(ObjectId),
                         quote=quote_.get("quote"),
                         tags=quote_.get("tags"))
            quot.save()    
            
if __name__ == '__main__':        
    load_authors()
