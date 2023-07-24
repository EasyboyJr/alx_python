#!/usr/bin/python3
import sys


# defining my function
def main():
    arguments = sys.argv[1:]
    argument_number = len(arguments)

    print("{}".format(argument_number), end=" ")
    if argument_number == 1:
        print("argument:")
    elif argument_number == 0:
        print("arguments", end=".\n")
        return
    else:
        print("arguments:")

    for num, arg in enumerate(arguments, 1):
        print("{}: {}".format(num, arg))


if __name__ == "__main__":
    main()
