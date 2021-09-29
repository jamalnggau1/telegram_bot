import re



def is_valid_email(email):
    if re.fullmatch(r"[^@]+@{1}[^@]+\.{1}[^@]+", email) is not None:

        return True
    else:
        return False