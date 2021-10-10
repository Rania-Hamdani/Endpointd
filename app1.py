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


Competencies_collection = database.get_collection('Competency')



@app.get("/get_Competencies")
def get_Competencies():
    Competencies = Competency.objects().to_json()
    Competencies_list = json.loads(Competencies)

    return{"Competencies": Competencies_list}  