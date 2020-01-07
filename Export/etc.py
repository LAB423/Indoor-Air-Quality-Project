import os
import csv
import pandas as pd 
import numpy  as np
from pymongo import MongoClient
import datetime
from pprint import pprint

# 1]  몽고디비에 연결

client = MongoClient("mongodb://Lab423:3240@203.255.67.238:27017")

db = client["test"] 

ColletionOfExperiment = db["experiment"]  # experiment table 
ColletionOfSensor =  db["sensor"]
deviceName_List = ColletionOfSensor.distinct("deviceName") 
sensorName_List = ColletionOfSensor.distinct("sensorname") 
unitName_List = ColletionOfSensor.distinct("unit")

sensor_Dict_JH = {
                    "OpenWindowsDistance1":"cm",
                    "OpenWindowsDistance2":"cm",
                    "Humidity":"%",
                    "Temperature":"*C",
                    "Flame1":"nm",
                    "Flame2":"nm",
                    "Sensor Value":"voc",
                    "TVOC":"ppb",
                    "CO2":"ppm",
                    "PM 1.0":"ug/m3",
                    "PM 2.5":"ug/m3",
                    "PM 10":"ug/m3",
                    "touchSensor":"touch",

                    }
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

sensorName_JH =[ key for key in sensor_Dict_JH.keys() ]
unitName_JH = [ sensor_Dict_JH[key] for key in sensor_Dict_JH.keys() ] 

sensorName_DB = [ key for key in sensor_Dict_DB.keys() ]
unitName_DB = [ sensor_Dict_DB[key] for key in sensor_Dict_DB.keys() ] 

def exportToCsv():
    for deviceName in deviceName_List:
        cursor = ColletionOfSensor.find(
                
                {

                "deviceName": deviceName,

                }, limit=3

                ).sort("_id",1)
        
        mongo_docs = pd.DataFrame(cursor)  
        pprint(mongo_docs)
        # time = "b"
        # timeDir = os.mkdir('C:\\test_ws\\'+ time)
        # # makeDirs = os.path.join(timeDir,)
        # print(timeDir)    
        mongo_docs.to_csv('C:\\test_ws\\' + deviceName +".csv")

def get_list_of_csv_files():

    list_of_files = os.listdir('C:\\test_ws\\')
    
    return list_of_files

 
def CsvToCsv():
    list_of_files = get_list_of_csv_files()
    print(list_of_files)

    for file in list_of_files:
        print("{}".format(file))
        c = open("{}".format(file), 'w') 
        print(type(c))
        reader = csv.reader(c)
    
        for line in reader:
            print(line)
        c.close()

exportToCsv()
CsvToCsv()