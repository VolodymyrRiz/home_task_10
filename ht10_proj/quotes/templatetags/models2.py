from datetime import datetime

from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import ObjectId, ReferenceField, BooleanField, DateTimeField, EmbeddedDocumentField, ListField, StringField


class Authors(Document):
    fullname = StringField()
    born_date = StringField()
    born_location = StringField()
    description = StringField()
    
class Quotes(Document):
    author = ReferenceField(Authors)
    quote = StringField()
    tags = ListField()
  

    
