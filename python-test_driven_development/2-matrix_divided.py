#!/usr/bin/python3
"""Module containing matrix_divided func"""


def matrix_divided(matrix, div):
    """Function for dividing all the elements of matrix"""

    # Checking if matrix is a list and its elements is lists containing ints
    if not (isinstance(matrix, list) and isinstance(i, list) for i in matrix
            and ((isinstance(a, int) for a in i) for i in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Checking if all rows containing same number of elements
    length = len(matrix)
    for i in range(length - 1):
        if len(matrix[i]) != len(matrix[i + 1]):
            raise TypeError("Each row of the matrix must have the same size")

    # Checking if div is not a float or int
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Checking if div is 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Dividing elements
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(element / div)
        new_matrix.append(new_row)

    # Return new matrix
    return new_matrix
