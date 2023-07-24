#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        print("{:2d} / {:2d} = {}". format(a, b, result))



print(safe_print_division(12, 2))
print(safe_print_division(12, 0))
