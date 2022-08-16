import re
import os
import re


def validarpass(ipasswd, iconfirmpasswd):
    if ipasswd != iconfirmpasswd:

        return False
    elif ipasswd == iconfirmpasswd:
        return True


def validate_email(email):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if (re.fullmatch(email_pattern, email)):
        return True
    else:
        return False
