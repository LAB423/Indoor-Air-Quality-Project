
# Connect MongoDB with flask server :
# -> https://medium.com/@riken.mehta/full-stack-tutorial-flask-react-docker-ee316a46e876

import os

from flask import Flask, render_template, request, jsonify
from flask_migrate import Migrate
from flask_pymongo import PyMongo 
from datetime import datetime
app = Flask(__name__)
# add mongo url to flask config, so that flask_pymongo can use it to make connection
app.config['MONGO_URI'] = os.environ.get('DB')
db = PyMongo(app, uri="mongodb://localhost:27017/test")

# initialize database migration management
# migrate = Migrate(app, db)

@app.route("/")
def hello():
    return "Hello World!"


# SAVE DATA TO DB
@app.route("/add", methods=["POST"]) 
def add():

    data = request.get_json()   
    ListOfDict = [ data[key] for key in data.keys() ] 
    deviceValue = ListOfDict[0].strip()   
    sensorName = ListOfDict[1].strip()   # "Huminity"
    value = ListOfDict[2].split()[0].strip()   # "33"
    unit = ListOfDict[2].split()[1].strip()    # "%"
    time = ListOfDict[3]

    dictionary = {

    "deviceName" : deviceValue,
    "sensorname"  :sensorName ,
    "value" : value,
    "unit" : unit,
    "time" : time

    }
    print(dictionary)
    db.db.sensor.insert_one(dictionary)
    return jsonify({'ok': True, 'message': 'Sensor created successfully!'}), 200
        
@app.route("/getlimit/<limit_>")
def get_limit(limit_):
    from Server_API_models import SensorData
    try:
        sensorData=SensorData.query.limit(limit_)
        return  jsonify([e.serialize() for e in sensorData])
    except Exception as e:
        return(str(e))

@app.route("/get/<id_>")
def get_by_id(id_):
    #from Server_API_models import SensorData
    try:
        sensorData=db.db.sensor.find_one_or_404({"unit":id_})
        return jsonify(sensorData)
    except Exception as e:
        return(str(e))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')