#!usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mat = []
    for row in matrix:
        new_row = list(map(lambda i: i ** 2, row))
        new_mat.append(new_row)
    return (new_mat)
