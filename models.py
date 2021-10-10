from mongoengine import Document, StringField, ListField

class Competency(Document):
     Competency = StringField
     Questions = ListField
     language_variations = ListField