#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # create a new variable that will hold the squared matrix
    squared_matrix = [[i ** 2 for i in row] for row in matrix]
    # return the new squared matrix
    return squared_matrix
