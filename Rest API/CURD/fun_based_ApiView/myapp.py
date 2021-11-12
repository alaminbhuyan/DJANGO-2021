from django.conf.urls import url
import requests
import json

URL = "http://127.0.0.1:8000/"
headers = {'content-Type' : 'application/json'}

# Read data through api
def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data) # convert python dictionary to json format
    r = requests.get(url=URL, headers=headers, data=json_data)
    data = r.json() # For respone message that will come in views.py file
    print(data)

# get_data()

# Create or Post data through api
def post_data():
    data = {
        'name' : 'Shamima Sultana',
        'roll' : 1053,
        'city' : "Comilla"
    }
    json_data = json.dumps(data) # convert python dictionary to json format
    r = requests.post(url=URL, headers=headers, data=json_data)
    data = r.json() # For respone message that will come in views.py file
    print(data)

# post_data()

# Update data through api
def update_data():
    data = {
        'id' : 6,
        'name' : 'Nahid bhuyan',
        'city' : "Rangpur"
    }
    json_data= json.dumps(data) # convert python dictionary to json format
    r = requests.put(url=URL, headers=headers, data=json_data)
    data = r.json() # For respone message that will come in views.py file
    print(data)

# update_data()

# Delete data through api
def delete_data():
    data = {'id' : 7}
    json_data = json.dumps(obj=data)# convert python dictionary to json format
    r = requests.delete(url=URL, headers=headers, data= json_data)
    data = r.json() # For respone message that will come in views.py file
    print(data)

# delete_data()