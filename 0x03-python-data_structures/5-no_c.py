#!/usr/bin/python3
def no_c(my_string):

    new = ""
    for e in my_string:
        if e not in 'cC':
            new += e
    return new
