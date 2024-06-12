#!usr/bin/python3
""""
Module divides element in marix
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): A matrix of integers or floats.
        div (int or float): The divisor.

    Returns:
        list of lists: A new matrix with each element divided by the divisor.

    Raises:
        TypeError: If the matrix is not a list of lists,
        or if the divisor is not a number.
        ZeroDivisionError: If the divisor is 0.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    if not matrix:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    if len(matrix) == 0 or any(len(row) == 0 for row in matrix):
        raise TypeError("Matrix must not be empty")

    row_length = len(matrix[0])

    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)
    return new_matrix
