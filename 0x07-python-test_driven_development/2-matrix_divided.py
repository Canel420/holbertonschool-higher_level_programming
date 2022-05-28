#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
2-matrix_divided.py module

"""


def matrix_divided(matrix, div):
    """
    Division of each element in matrix

    Parameters
    ----------
    matrix: Square matrix
    div: Integer/float for each element division

    Returns
    -------
    New matrix with element divided

    Raises
    ------
    TypeError: if matrix elements or div parameter are not
               type integer/float, or if is not a squared
               matrix.
    ZeroDivisionError: if div parameter is zero.

    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    for row in range(len(matrix)):
        if row <= len(matrix) - 2 and len(matrix[row]) != len(matrix[row + 1]):
            raise TypeError("Each row of the matrix must have the same size")
        for item in range(len(matrix[row])):
            if type(matrix[row][item]) not in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")

    return list(map(lambda row: list(map(lambda x: round((x / div), 2), row)),
                matrix))
