
import os
import json
from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo 
from pymongo import MongoClient
import datetime
from pprint import pprint

app = Flask(__name__)
app.config['MONGO_URI'] = os.environ.get('DB')

db = PyMongo(app, uri="mongodb://localhost:27017/test")

def get_list_of_json_files():
    
    list_of_files = os.listdir('descriptions')  # creates list of all the files in the folder
    return list_of_files


def create_list_from_json(collecion):

    with open(collecion) as f:
        data = json.load(f)
    
    data_list = []
    data_list.append(data['_id'])   

    # In few json files, the race was not there so using KeyError exception to add '' at the place
    try:
        data_list.append(data['meta']['unstructured']['race'])
    except KeyError:
        data_list.append("")  # will add an empty string in case race is not there.
    data_list.append(data['name'])

    return data_list


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

    # date1 = datetime.datetime.utcnow()-datetime.timedelta(minutes=15)
    # date1 = date1.strftime("%Y-%m-%dT%H:%M:%S.000Z")
    # print(date1) #2019-12-15T08:17:31.000Z
    # pprint(ColletionOfSensor.find({'time':{"$lt":date1}}).count()) #855626

    # for cursor in  ColletionOfSensor.find({'time':{"$lt":date1}}):
    #     pprint(cursor)


# 하루날짜로 데이터 수집하기 
#https://dba.stackexchange.com/questions/112179/date-range-query-for-past-24-hour-in-mongo-shell
