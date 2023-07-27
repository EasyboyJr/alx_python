#!/usr/bin/python3
def best_score(a_dictionary):
    # check if the dictionary is empty. if empty, return none
    if not a_dictionary:
        return None
    # create variable to initialize the return and set to 0 they will be placeholder for our return 
    highest_score = int("0")
    # initially set the best key to none
    best_key = None
    # iterate over the a_dictionary to check for the highest score 
    for key, value in a_dictionary.items():
        # if value is greater than highest score chenge higest score to the value and change the best key to the new key
        if value > highest_score:
            highest_score = value
            best_key = key
        # return the new best key
    return best_key
