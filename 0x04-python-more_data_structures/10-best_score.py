#!/usr/bin/python3
def best_score(a_dictionary):
    max = 0
    name = None
    if not a_dictionary:
        return name

    for k, v in a_dictionary.items():
        if (v > max):
            max = v
            name = k
    return name
