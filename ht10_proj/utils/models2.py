from datetime import datetime

from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import ObjectId, ReferenceField, BooleanField, DateTimeField, EmbeddedDocumentField, ListField, StringField


class Author(Document):
    fullname = StringField()
    born_date = StringField()
    born_location = StringField()
    description = StringField()
    
class Quote(Document):
    author = ReferenceField(Author)
    quote = StringField()
    tags = ListField()
  

    
