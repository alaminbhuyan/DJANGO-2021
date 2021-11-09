import requests
import json


# This could be any application like mobile app, computer applications and so on.

URL = "http://127.0.0.1:8000/"

data = {
    'name': "fatema",
    'roll': 1031,
    'city': "Dhaka"
}

json_data = json.dumps(data)
print(json_data)

r = requests.post(url=URL, data=json_data)

data2 = r.json()

print(data2)