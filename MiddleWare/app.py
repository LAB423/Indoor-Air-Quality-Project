# pySerial API : https://pyserial.readthedocs.io/en/latest/pyserial_api.html

import serial
from datetime import datetime
import time
time.sleep(1)

ser = serial.Serial('COM15', 9600) # Serial(Comport,baudrate)
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
        # .replace("\r\n","") "\r\n"를 "" 공백으로 바꿔주기
        # .rstrip() 리스트의 오른쪽 공백 없애주기  
        # > 여기서 꼭 필요한 건 아니지만 " " 공백은 문자열로 인식됨으로 없애서 저장하는 것이 좋음 
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # 센서가 측정된 시간으로 저장하기 

        import requests 
        API_ENDPOINT = "http://203.255.67.238:5000/add"  # api로 요청할 데이터를 전송할 서버 주소 설정

        formData = {
            
            'deviceName': "place2",
            'sensorName': sensorName, 
            'sensorValue' : sensorValue,
            'time' : time
        }
        
        response = requests.post(url = API_ENDPOINT, json = formData) # 받은 데이터를 json형식으로 보내는 걸로 응답하기 
        print(formData)
           
    except:
        print("오류 발생")
        continue # 오류가 발생하더라도 계속 진행  
        
