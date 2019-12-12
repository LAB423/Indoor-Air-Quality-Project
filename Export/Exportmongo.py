
from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017")

db = client["test"]  # 
collection_list = db.collection_names() # 테이블 출력하기 
print(collection_list)

ColletionOfExperiment = db["experiment"]  # experiment 테이블 출력하기
ColletionOfSensor =  db["sensor"]


results = ColletionOfSensor.find()  #전체데이터조회

# for result in results:
#     print(result)
