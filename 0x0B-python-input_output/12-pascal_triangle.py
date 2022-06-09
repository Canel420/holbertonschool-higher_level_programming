#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Function pascal_triangle """


def pascal_triangle(n):
    """
    Pascal triangle recomputing line
    right to left.

    Parameters
    ----------
    n: number of rows
    """
    answer = []

    for row in range(n):
        answer.append(1)  # both widen the row and initialize last element

        for i in range(row - 1, 0, -1):  # fill in the row, right to left
            answer[i] += answer[i - 1]  # current computed from previous

        print(answer)
