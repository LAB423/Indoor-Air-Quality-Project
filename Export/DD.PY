import pandas as pd 
import numpy as np 
from pprint import pprint
import csv
import codecs

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


# 1. 원본 데이터프레임
columns1 = ['id','sensorname', 'value', 'unit','time']
aa = pd.DataFrame(columns=columns1)

# data 
a = sensorName_DB
b = [str(i) for i in range(len(a))]

# data 채우기
for i in range(len(columns1)):
    aa[columns1[i]] = b 
aa[columns1[1]] = a
aa["time"] =np.random.randint(5)
pprint(aa)


pprint(type(aa[columns1[1]])) # Series = 데이터프레임의 하나의 컬럼 

# 2. .csv file 저장 
aa.to_csv("test.csv")

# 3. 저장할 dataFrame 구조만들기 

# 센서이름 리스트로 필드이름(column)설정 
columns = sensorName_DB[:len(a)] #+ ["year", "month","day","time"] 
reDataFrame = pd.DataFrame(columns=columns)

# 4. csv 파일 읽기 
c = pd.read_csv(
    "test.csv",
    index_col=0, # 지정되지 않은 인덱스 컬럼 지우기 
    # parse_date =[],
    # na_values =[],
    )
print(c)
print(type(c))

# 인덱스 단위로 데이터 전체 불러오기 
# 1)  sensorname, value , unit 값만 따로 불러들이기 
#     5번 !!
# 2)  time -> 년, 월, 일 , 시간 으로 나눠서 저장하기 

for indexNumer in range(len(c.index)):
    data  = c.loc[
                indexNumer,
                ["sensorname","value","unit"]
            ]
    print(type(data["value"]))
    # print(columns[indexNumer])
    if data["sensorname"] == "":continue
    elif data["sensorname"] == columns[indexNumer]:
        data = {
                
            }
        reDataFrame.columns[indexNumer] = data["value"]

    print(reDataFrame)

    print(type(data))

    # print(type(c.loc[indexNumer,]))  # series 
 
# 5. sensorname 리스트에 value 값을 입력해야함!
# for sensorname in columns:
#     if c[columns[sensorname]] == sensorname:
#         c[columns[sensorname]] 

# 6. 원래 csv 파일에 저장하기 


# csv 파일 로드하기 
# https://www.shanelynn.ie/python-pandas-read_csv-load-data-from-csv-files/

# pandas 기본 
# https://sacko.tistory.com/52

# 특정조건 주어서 pandas column 값 변경하기 
# https://openmymind.tistory.com/entry/Pandas-%ED%8A%B9%EC%A0%95-%EC%A1%B0%EA%B1%B4%EC%9D%B8-%EA%B2%BD%EC%9A%B0-column%EA%B0%92-%EB%B3%80%EA%B2%BD%ED%95%98%EA%B8%B0