from django.conf.urls import url
import requests
import json

URL = "http://127.0.0.1:8000/"

# Read data through api
def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data) # convert python dictionary to json format
    r = requests.get(url=URL, data=json_data)
    data = r.json() # For respone message that will come in views.py file
    print(data)

# get_data()

# Create or Post data through api
def post_data():
    data = {
        'name' : 'Karim',
        'roll' : 1037,
        'city' : "Dhaka"
    }
    json_data = json.dumps(data) # convert python dictionary to json format
    r = requests.post(url=URL, data=json_data)
    data = r.json() # For respone message that will come in views.py file
    print(data)

post_data()

# Update data through api
def update_data():
    data = {
        'id' : 4,
        'name' : 'Mim sultana',
        'city' : "Rangpur"
    }
    json_data= json.dumps(data) # convert python dictionary to json format
    r = requests.put(url=URL, data=json_data)
    data = r.json() # For respone message that will come in views.py file
    print(data)

# update_data()

# Delete data through api
def delete_data():
    data = {'id' : 3}
    json_data = json.dumps(obj=data)# convert python dictionary to json format
    r = requests.delete(url=URL, data= json_data)
    data = r.json() # For respone message that will come in views.py file
    print(data)

# delete_data()