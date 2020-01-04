import os
import json
import pandas
from pymongo import MongoClient
import datetime
from pprint import pprint

# 1]  몽고디비에 연결

client = MongoClient("mongodb://Lab423:3240@203.255.67.238:27017")

db = client["test"] 
# collection_list = db.list_collection_names()
# print(collection_list) # collection(테이블) 호출

ColletionOfExperiment = db["experiment"]  # experiment table 
ColletionOfSensor =  db["sensor"]

# 시리얼 통신을 통해 DB에 저장된 컬럼리스트 내용파악 
# 1. deviceName 리스트 
deviceName_List = ColletionOfSensor.distinct("deviceName") #deviceName 필드 조회
# print(deviceName_List)

# # 2. sensorName 리스트 
# sensorName_List = ColletionOfSensor.distinct("sensorname") #sensorname 필드 조회
# print(sensorName_List)
# print(len(sensorName_List))

# # 3. unitName 리스트 
# unitName_List = ColletionOfSensor.distinct("unit")
# print(len(unitName_List))


# 디비에 저장되어야 하는 sensorName, unit 리스트내역파악 
# -> 시리얼통신오류로 디비에 잘못저장된 센서리스트들이 있어서 마련함 

# place2JH에 저장되어야하는 {센서이름 : unit } dict 
sensor_Dict_JH = {
                    "OpenWindowsDistance1":"cm",
                    "OpenWindowsDistance2":"cm",
                    "Humidity":"%",
                    "Temperature":"*C",
                    "Flame1":"nm",
                    "Flame2":"nm",
                    "Sensor Value":"voc",
                    "Vol":"vol",
                    "ppm":"ppm",
                    "PM 1.0":"ug/m3",
                    "PM 2.5":"ug/m3",
                    "PM 10":"ug/m3",
                    "touchSensor":"touch",

                    }
# place1에 저장되어야하는 {센서이름 : unit } dict 
sensor_Dict_DB = {
                    "Humidity":"%",
                    "Temperature":"*C",
                    "Flame1":"nm",
                    "Flame2":"nm",
                    "Sensor Value":"voc",
                    "Vol":"vol",
                    "ppm":"ppm",
                    "PM 1.0":"ug/m3",
                    "PM 2.5":"ug/m3",
                    "PM 10":"ug/m3",
                    "touchSensor":"touch",

                    }

# place2JH - sensorName , unitName 리스트 따로 출력 
sensorName_JH =[ key for key in sensor_Dict_JH.keys() ]
unitName_JH = [ sensor_Dict_JH[key] for key in sensor_Dict_JH.keys() ] 

# place1 - sensorName , unitName 리스트 따로 출력 
sensorName_DB = [ key for key in sensor_Dict_DB.keys() ]
unitName_DB = [ sensor_Dict_DB[key] for key in sensor_Dict_DB.keys() ] 




for deviceName in deviceName_List:
# make an API call to the MongoDB server using a Collection object
    cursor = ColletionOfSensor.find(
            {
            #       key :   value - 전체조회
            "deviceName": deviceName,
            # "unit" :'ug/mr'
            }, limit=3

            ).sort("_id", -1)
    print(type(cursor))
    mongo_docs = list(cursor) 
    
    mongo_docs = mongo_docs[:5]
    pprint(mongo_docs)
    print(type(mongo_docs[0]))

docs = pandas.DataFrame(columns=[])
for num, doc in enumerate(mongo_docs):
    doc["Temperature"] = str(doc["Temperature"])
    doc_id = doc["Temperature"]

# create a Series obj from the MongoDB dict
series_obj = pandas.Series( doc, name=doc_id )

# append the MongoDB Series obj to the DataFrame obj
docs = docs.append(series_obj)
docs.to_json("object_rocket.json")
json_export = docs.to_json()    