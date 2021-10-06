from request_to_server.requests import login
from constants import machine_token_constant


def filling_skills_check(telegram_id):
    request_from_login = login(telegram_id, machine_token_constant)
    if request_from_login.status_code == 200:
        if len(request_from_login.json().get("skills")) > 0:
            return True
        else:
            return False

    else:
        return "Error"
