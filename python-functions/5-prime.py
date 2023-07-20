#!/usr/bin/python3
def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    max_divider = int(number ** 0.5) + 1
    for i in range(3, max_divider, 2):
        if number % i == 0:
            return False
    return True
