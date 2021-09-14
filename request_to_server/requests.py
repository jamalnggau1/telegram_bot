import json
from constants import host
import requests


def registration(user_id, full_name, email):
    url = host + "/filling_profile/users/"

    payload = json.dumps({
        "profile": {
            "contacts": user_id,
            "full_name": full_name,
            "email": email
        }
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response



def login(user_id=None, machine_token=None):
    url = host + "/filling_profile/users/login/"

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


def patch(meeting_status=None, token_value=None):
    if meeting_status is not None:
        payload_data = {"meeting_status": meeting_status}

    payload_dict = {"profile": payload_data}

    payload = json.dumps(payload_dict)

    url = host + "/filling_profile/user/"

    token = 'Bearer ' + token_value
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }

    response = requests.request("PATCH", url, headers=headers, data=payload)

    return response.status_code


def leave_feedback(profile_id, machine_token, feedback):
    url = host + "/filling_profile/leave_feedback/"

    payload = json.dumps({
        "profile_id": profile_id,
        "machine_token": machine_token,
        "feedback": feedback
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response
