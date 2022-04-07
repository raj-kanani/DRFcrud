import json
import requests

# this file is client frontend data store


# deserialization data json into string convert.


url = "http://127.0.0.1:8000/student/"


# # # create student

def add_data():
    data = {
        'name': 'rutvik',
        'roll': 100,
        'city': 'mumbai'
    }
    headers = {'content-Type': 'application/json'}

    json_data = json.dumps(data)
    r = requests.post(url=url, headers=headers, data=json_data)
    data = r.json()
    print(data)


add_data()


# get , update and delete data
def get_data(id=None):
    data = {}
    if id is not None:
        data = {"id": id}
    json_data = json.dumps(data)
    r = requests.get(url=url, data=json_data)
    data = r.json()
    print(data)
    return data


get_data()


def update_data():
    data = {
        'id': 9,
        'name': 'abc',
        'roll': 123,
        'city': 'pune'
    }

    json_data = json.dumps(data)
    r = requests.put(url=url, data=json_data)
    data = r.json()
    print(data)


# update_data()


def delete_data():
    data = {
        'id': 4,
    }
    json_data = json.dumps(data)
    r = requests.delete(url=url, data=json_data)
    data = r.json()
    print(data)

# delete_data()
