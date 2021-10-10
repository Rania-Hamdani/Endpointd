from mongoengine import Document, StringField, ListField

class PresetRole(document):
     language_variations = ListField
     top_competencies = ListField
     secondary_competencies= ListField
