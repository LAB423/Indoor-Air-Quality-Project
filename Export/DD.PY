import pandas as pd 

a= [str(i) for i in range(0,3)]
print(a)

index = ["mi", "da", "jung"]

for j in a:
    aa = pd.DataFrame(a)
    aa.to_csv(str(j)+".csv")
 
    
# import pandas as pd 
# from pprint import pprint

# name = ["a","b","c","d"]


# cursor = [{'_id': "ws",
#   'deviceName': 'a',
#   'sensorname': 'Temperature',
#   'time': '2019-12-10 16:05:05',
#   'unit': '*C',
#   'value': '90'},
#  {'_id': "ws",
#   'deviceName': 'a',
#   'sensorname': 'Flame1',
#   'time': '2019-12-10 16:05:05',
#   'unit': '*C',
#   'value': '90'},
#  {'_id': "ws",
#   'deviceName': 'a',
#   'sensorname': 'Flame2',
#   'time': '2019-12-10 16:05:05',
#   'unit': '*C',
#   'value': '90'}]

# i = 0

# test = pd.DataFrame(cursor)
# for i in range(len(name)):
#     test.to_csv("C:\\test_ws\\"+str(name[i])+".csv")
