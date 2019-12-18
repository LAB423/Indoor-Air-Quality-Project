# pySerial API : https://pyserial.readthedocs.io/en/latest/pyserial_api.html

import serial
from datetime import datetime
import time
time.sleep(1)

ser = serial.Serial('/dev/ttyACM0', 9600) # Serial(Comport,baudrate)
ser.flushInput()

while True:
    try:
        # 1. 아두이노에서 받은 시리얼값 받아서 처리하기 
        
        serial = ser.readline().decode() # 1초 동안 받아들여진 시리얼값을 문자열로 인코딩 
        # print(serial) # " ppm: 1.00 ppm "
        sensor = serial.split(":")  # .split(":") 로 센서이름이랑 측정값 리스트로 담기
        # print(sensor)   # ['ppm', '1.00 ppm \r\n '] 
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