#!/usr/bin/python3
def fibonacci_sequence(n):
    fibonacci_seq = [0, 1]
    for i in range(2, n):
        next_num = (fibonacci_seq[-1]) + (fibonacci_seq[-2])
        fibonacci_seq.append(next_num)
    if n == 1:
        return [0]
    elif n >= 2:
        return fibonacci_seq
    else:
        return []
