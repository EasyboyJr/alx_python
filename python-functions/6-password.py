#!/usr/bin/python3
def validate_password(password):
    lenght = len(password)
    if lenght < 8:
        return False
    
    upper = lower = digit = False
    for i in password:
        if i.isupper():
            upper = True
        elif i.islower():
            lower = True
        elif i.isdigit():
            digit = True

        if i.isspace():
            return False

    if upper and lower and digit == True:
        return True
    else:
        return False
