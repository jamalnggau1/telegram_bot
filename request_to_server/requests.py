import json
from constants import host
import requests


def registration(user_id, full_name, email):
    url = host + "/api/users/"

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
    url = host + "/api/users/login/"

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

def stop_meet_change_partner(profile_telegram, machine_token):
    url = host + "/api/stop_meet_change_partner/"

    payload = json.dumps({

        "profile_id": profile_telegram,
        "machine_token": machine_token,
    })
    headers = {
        'Content-Type': 'application/json'
    }

    return requests.request("POST", url, headers=headers, data=payload)



def getfeedbackfromuser(user_telegram):
    url = host + "/api/getfeedbackfromuser/"

    payload = json.dumps({
        "user_telegram": user_telegram
    })
    headers = {'Content-Type': 'application/json'}
    return requests.request("POST", url, headers=headers, data=payload)


def patch(meeting_status=None, token_value=None):
    if meeting_status is not None:
        payload_data = {"meeting_status": meeting_status}

    payload_dict = {"profile": payload_data}

    payload = json.dumps(payload_dict)

    url = host + "/api/user/"

    token = 'Bearer ' + token_value
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }

    response = requests.request("PATCH", url, headers=headers, data=payload)

    return response.status_code


def leave_feedback(profile_id, machine_token, feedback):
    url = host + "/api/leave_feedback/"

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
