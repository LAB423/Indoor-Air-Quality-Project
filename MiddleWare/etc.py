import serial
from datetime import datetime
import time
time.sleep(1)

ser = serial.Serial('/dev/ttyACM0', 9600) # Serial(Comport,baudrate)
ser.flushInput()


while True:
    try:
        SVT = []
        serial = ser.readline().decode()
        SVT = serial.split(",")
        sensorToList = [x.strip() for x in SVT if x.strip()]
        sensor =   [ oneSensor.split(":")  for oneSensor in sensorToList ]

        for Value in sensor:   
            sensorName = Value[0].strip()
            sensorValue = Value[1].strip()


            time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            import requests 
            API_ENDPOINT = "http://203.255.67.238:5000/add"

            formData = {
                
                'deviceName': "place1",
                'sensorName': sensorName, 
                'sensorValue' : sensorValue,
                'time' : time
            }
            response = requests.post(url = API_ENDPOINT, json = formData) 
            print(formData)

    except:
        print("Error")
        continue 