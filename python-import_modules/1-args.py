#!/usr/bin/python3
import sys
def main():
    arguments = sys.argv[1:]
    argument_number = len(arguments)
    print("{}".format(argument_number), end=" ")
    if argument_number == 1:
        print("argument:")
    elif argument_number == 0:
        print("arguments",end="")
    else:
        print("arguments:")
    if argument_number > 0:
        print()
    else:
        print(".", end="\n")
        return
    for num in enumerate(arguments, 1):
        print("{}: {}".format(num, arguments))

        
if __name__ == "__main__":
    main()