import pandas as pd 
from pprint import pprint

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


sensorName_DB = [ key for key in sensor_Dict_DB.keys() ]
unitName_DB = [ sensor_Dict_DB[key] for key in sensor_Dict_DB.keys() ] 


# ㅉㅣㄴ dataFrame ㅂㅕㄴㅅㅜ
a = [ i  for i in "apple" ]
b = [str(i) for i in range(len(a))]
columns = sensorName_DB[:len(a)] # 센서이름 리스트로 설정 
# pprint(columns[1])

# dataFrame
aa = pd.DataFrame([a,b], columns=columns)
pprint(aa[columns[1]].T)

# .csv file ㅁㅏㄴㄷㅡㄹㄱㅣ
for j in b:
    aa.to_csv(str(j)+".csv")

# pprint(aa)
