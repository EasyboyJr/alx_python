#!/usr/bin/python3
# define the fuction that checks for c or C and return back the string without c or C
def no_c(my_string):
    # create a cariable that hold the new string
    new_string = ""
    # use a for loop to iterate over my_string
    for char in my_string:
        #check if each iteration is a c or C by checking the lower case form
        if char.lower() != "c":
            # if char.lower is not c add the iteration char to the new string variable
            new_string += char
    # return the new string
    return new_string
