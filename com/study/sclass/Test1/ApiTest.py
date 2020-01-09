import requests
import json

data = {
    "dbName": "UBAINS2",
    "dbType": 0,
    "searchType": 2
}

url = 'http://124.206.6.6:8210/face/createdb'
rsp = requests.post(url, data=json.dumps(data), headers="", verify=False)

statusCode = rsp.text
print(statusCode)
