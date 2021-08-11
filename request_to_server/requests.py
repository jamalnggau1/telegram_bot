import json

import requests


def login(user_id = None, machine_token=None ):
    url = "http://127.0.0.1:8000/filling_profile/users/login/"

    payload = json.dumps({
        "profile": {
            "contacts": user_id,
            "machine_token": machine_token
        }
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response

def patch(meeting_status = None, token_value = None):

    if meeting_status !=None:
        payload_data = {"meeting_status":meeting_status}

    payload_dict = {"profile":payload_data}

    payload = json.dumps(payload_dict)


    url = "http://127.0.0.1:8000/filling_profile/user/"


    token = 'Bearer '+token_value
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }

    response = requests.request("PATCH", url, headers=headers, data=payload)

    return response.status_code



