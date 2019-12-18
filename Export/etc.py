import os
import json
import pandas
from pymongo import MongoClient
import datetime
from pprint import pprint


client = MongoClient("mongodb://Lab423:3240@203.255.67.238:27017")

db = client["test"] 
collection_list = db.list_collection_names()
print(collection_list)

ColletionOfExperiment = db["experiment"]  # experiment table 
ColletionOfSensor =  db["sensor"]

deviceName_List = ColletionOfSensor.distinct("deviceName")
print(type(deviceName_List))

sensorName_List = ColletionOfSensor.distinct("sensorname")
print(sensorName_List)
print(len(sensorName_List))
unitName_List = ColletionOfSensor.distinct("unit")
print(unitName_List)

for i in deviceName_List:
# make an API call to the MongoDB server using a Collection object
    cursor = ColletionOfSensor.find(
            
            {
            #       key :   value - 전체조회
            "unit":  'ug/m3OpenWindowsDistance2'#deviceName_List[i]

            }, limit =3
            ).sort("_id", -1)
    mongo_docs = list(cursor) 
    # mongo_docs = mongo_docs[:5]
    pprint(mongo_docs)

    docs = pandas.DataFrame(columns=[])
    for num, doc in enumerate(mongo_docs):
        doc["_id"] = str(doc["_id"])
        doc_id = doc["_id"]

    # create a Series obj from the MongoDB dict
    series_obj = pandas.Series( doc, name=doc_id )

    # append the MongoDB Series obj to the DataFrame obj
    docs = docs.append(series_obj)
    docs.to_json("object_rocket.json")
    json_export = docs.to_json()    