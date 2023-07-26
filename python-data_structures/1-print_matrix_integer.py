#!/usr/bin/python3
# declare a function that prints out a matrix in format
def print_matrix_integer(matrix=[[]]):
    # use a nested for loop to iterate over the matrix and each row
    for row in matrix:
        for num in row:
            print("{:d}".format(num), end=" ")
        print(end="\n")
