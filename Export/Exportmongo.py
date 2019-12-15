
from pymongo import MongoClient
import json
from pprint import pprint
import datetime

if __name__ == '__main__':
    client = MongoClient("mongodb://Lab423:3240@203.255.67.238:27017")

    db = client["test"] 
    collection_list = db.list_collection_names()
    print(collection_list)

    ColletionOfExperiment = db["experiment"]  # experiment table 
    ColletionOfSensor =  db["sensor"]

    # results = ColletionOfSensor.find({},limit=3)  #전체데이터조회
    # for result in results:
    #     pprint(result)

    date1 = datetime.datetime.utcnow()-datetime.timedelta(minutes=15)
    date1 = date1.strftime("%Y-%m-%dT%H:%M:%S.000Z")
    print(date1)
    for cursor in  ColletionOfSensor.find({'time':{"$lt":date1}}):
        pprint(cursor)



# 하루날짜로 데이터 수집하기 
#https://dba.stackexchange.com/questions/112179/date-range-query-for-past-24-hour-in-mongo-shell
