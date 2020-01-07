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
# collection_list = db.list_collection_names()
# print(collection_list) # collection(테이블) 호출

ColletionOfExperiment = db["experiment"]  # experiment table 
ColletionOfSensor =  db["sensor"]

# 시리얼 통신을 통해 DB에 저장된 컬럼리스트 내용파악 
# 1. deviceName 리스트 
deviceName_List = ColletionOfSensor.distinct("deviceName") #deviceName 필드 조회
# print(deviceName_List)

# 2. sensorName 리스트 
sensorName_List = ColletionOfSensor.distinct("sensorname") #sensorname 필드 조회
# print(sensorName_List)
# print(len(sensorName_List))

# 3. unitName 리스트 
unitName_List = ColletionOfSensor.distinct("unit")
# print(len(unitName_List))


# 디비에 저장되어야 하는 sensorName, unit 리스트내역파악 
# -> 시리얼통신오류로 디비에 잘못저장된 센서리스트들이 있어서 정확한 센서 이름들만 집합함 

# place2JH에 저장되어야하는 {센서이름 : unit } dict 
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

# 2] csv 형식으로 출력하기 
def exportToCsv():
    for deviceName in deviceName_List:
    # make an API call to the MongoDB server using a Collection object

    #find() 결과는 cursor 로 출력 
    # => json 객체로 바꿔서 사용하거나, DataFrame으로 변환해서 사용한다
        cursor = ColletionOfSensor.find(
                
                {
                #       key :   value - 전체조회
                "deviceName": deviceName,

                }, limit=3

                ).sort("_id",1)
        
        mongo_docs = pd.DataFrame(cursor)  # cursor를 dict 타입으로 바꾸기 
        pprint(mongo_docs)
        # time = "b"
        # timeDir = os.mkdir('C:\\test_ws\\'+ time)
        # # makeDirs = os.path.join(timeDir,)
        # print(timeDir)    
        mongo_docs.to_csv('C:\\test_ws\\' + deviceName +".csv")

# 파일 불러오기
def get_list_of_csv_files():

    list_of_files = os.listdir('C:\\test_ws\\')
    
    return list_of_files

# 3] csv 형식으로 변환하기 
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
    # results = ColletionOfSensor.find({},limit=3)  #전체데이터조회
    # for result in results:
    #     pprint(result)

    # date1 = datetime.datetime.utcnow()-datetime.timedelta(minutes=15)
    # date1 = date1.strftime("%Y-%m-%dT%H:%M:%S.000Z")
    # print(date1) #2019-12-15T08:17:31.000Z
    # pprint(ColletionOfSensor.find({'time':{"$lt":date1}}).count()) #855626

    # for cursor in  ColletionOfSensor.find({'time':{"$lt":date1}}):
    #     pprint(cursor)


# 하루날짜로 데이터 수집하기 
#https://dba.stackexchange.com/questions/112179/date-range-query-for-past-24-hour-in-mongo-shell
