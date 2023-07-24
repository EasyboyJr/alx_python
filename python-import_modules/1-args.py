
import sys
def main():
    arguments = sys.argv[1:]
    argument_number = len(arguments)

    print("{}".format(argument_number), end=" ")
    if argument_number == 1:
        print("argument:", end=" ")
    else:
        print("arguments:", end=" ")
    
    if argument_number > 0:
        print()
    else:
        print(".", end="\n")
        return
    