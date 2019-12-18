# pySerial API : https://pyserial.readthedocs.io/en/latest/pyserial_api.html

import serial
from datetime import datetime
import time
time.sleep(1)

ser = serial.Serial('/dev/ttyACM0', 9600) # Serial(Comport,baudrate)
ser.flushInput()

while True:
    try:
        serial = ser.readline().decode() 
        sensor = serial.split(":")  
        sensorName = sensor[0]  # 'ppm'
        sensorValue = sensor[1].replace("\r\n","").rstrip() # 1.00 ppm
       
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
        
           
    except:
        print("Error")
        continue

print("End")