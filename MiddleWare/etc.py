import serial
from datetime import datetime
import time
time.sleep(1)

ser = serial.Serial('COM15', 9600) # Serial(Comport,baudrate)
ser.flushInput()


while True:
    try:
        SVT = []
        SVT = serial.split(",")
        sensorToList = [x.strip() for x in SVT if x.strip()]
        sensor =   [ oneSensor.split(":")  for oneSensor in sensorToList ]
        print(sensor)

        sensorValue = [] 
        for Value in sensor:   
            print(Value)
            sensorName = Value[0].strip()
            sensorValue = Value[1].strip()

        print(sensorName , sensorValue)

        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        import requests 
        API_ENDPOINT = "http://203.255.67.238:5000/add"

        formData = {
            
            'deviceName': "place2",
            'sensorName': sensorName, 
            'sensorValue' : sensorValue,
            'time' : time
        }
        response = requests.post(url = API_ENDPOINT, json = formData) 
        print(formData)

    except:
        print("오류 발생")
        continue 