#!/usr/bin/python3
# declare a function that prints out a matrix in format
def print_matrix_integer(matrix=[[]]):
    # use a nested for loop to iterate over the matrix and each row
    for row in matrix:
        for num in row:
            print("{:d}".format(num), end=" ")
        print(end="\n")



matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
