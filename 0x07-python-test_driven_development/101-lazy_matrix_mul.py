#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" 101-lazy_matrix_mul module """
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices

    Parameter
    ---------
    m_a: First matrix.
    m_b: Second matrix.

    Return
    ------
    Product of two matrices
    """
    return (np.dot(m_a, m_b))
