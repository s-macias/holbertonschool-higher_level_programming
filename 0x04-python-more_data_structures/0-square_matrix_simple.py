#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    my_matrix = matrix.copy()
    my_matrix = [[x * x for x in row] for row in matrix]
    return(my_matrix)
