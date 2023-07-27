#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    # multiply each item in my list by number 
    new_list = map(lambda x: x * number, my_list)
    # return new lust
    return list(new_list)
