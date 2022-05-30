#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" 100-matrix_mul module """


def check_matrix(matrix, name):
    """
    Check if a matrix is appropiate
    for multiplication.

    Parameter
    ---------
    matrix: matrix to check.
    name: name of the matrix for errors.

    Raise
    -----
    ValueError: if matrix is empty.
    ValueError: if some of the rows are empty.
    TypeError: if element of the matrix are not
               integers or floats.
    TypeError: if rows of matrix are not lists.
    TypeError: if rows does not have the same size.
    TypeError: if matrix is not a list.
    """
    if type(matrix) is list:
        if len(matrix) == 0:
            raise ValueError(name + " can't be empty")
        for row in matrix:
            if type(row) is list:
                if len(row) == 0:
                    raise ValueError(name + " can't be empty")
                else:
                    for elm in row:
                        if type(elm) not in [int, float]:
                            raise TypeError(name + " should contain only " +
                                            "integers or floats")
            elif type(row) is not list:
                raise TypeError(name + " must be a list of lists")
            if len(row) != len(matrix[0]):
                raise TypeError("each row of " + name + " must be of the " +
                                "same size")
    else:
        raise TypeError(name + " must be a list")


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices

    Parameters
    ----------
    m_a: First matrix.
    m_b: Second matrix.

    Returns
    -------
    Resulting matrix.

    Raises
    ------
    ValueError: if matrices can not be multiplied.
    """
    check_matrix(m_a, 'm_a')
    check_matrix(m_b, 'm_b')
    A_cols = len(m_a[0])
    B_rows = len(m_b)

    if A_cols == B_rows:
        result = [[sum(a * b for a, b in zip(A_row, B_col))
                  for B_col in zip(*m_b)]
                  for A_row in m_a]
        return (result)
    else:
        raise ValueError("m_a and m_b can't be multiplied")
