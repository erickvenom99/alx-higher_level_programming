def matrix_divided(matrix, div):
    """
    Divide all rows in matrix by div

    Args:
        matrix (list of lists): Matrix containing float or integer elements.
        div (int or float): Divisor.

    Returns:
        list of lists: New matrix containing the result of division by div, rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floating-point numbers,
                   if each row in the matrix is not of the same size,
                   or if div is not an integer or a floating-point number.
        ZeroDivisionError: If div is equal to 0.
    """

if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

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
