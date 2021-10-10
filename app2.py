from fastapi import FastAPI
from pymongo.database import Database
from models import Competency
from mongoengine import connect  
import json
import pymongo
import ssl

app= FastAPI()
client = pymongo.MongoClient('mongodb+srv://Rania_Hamdeni:careerboosts2000@cluster0.vfuyb.mongodb.net/test', ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
database = client.CareerBoosts


Competencies_collection = database.get_collection("Competency")
PrestRole_collection = database.get_collection("PresetRole")




@app.get("/get_CompetenciesbyRole/{_id}")
def get_CompetenciesbyRole(_id):
    competencies = PresetRole.objects.get(_id=_id)

    competencies_dict = { 
        "top_competencies": Competency.language_variations()
    }
    return competencies_dict 