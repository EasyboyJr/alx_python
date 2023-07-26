#!/usr/bin/python3
# declare a function that prints out a matrix in format
def print_matrix_integer(matrix=[[]]):
    # if matrix is empty, just print an empty line and return 
    if not matrix:
        print()
        return
    # iterate over each row in the matrix
    for row in matrix:
        # if row is empty print a new line and skip to next row 
        if not row:
            print()
            continue
        # iterate over each element in row using enumerate
        for i, num in enumerate(row):
            # if it is the last element in row print element folowed by a new line 
            if i == len(row) -1:
                print("{:d}".format(num))
            # else if it is not the last print element followed by a space
            else:
                print("{:d}".format(num), end=" ")
