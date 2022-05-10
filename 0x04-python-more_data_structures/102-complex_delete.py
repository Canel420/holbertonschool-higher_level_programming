#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    remove = {k: v for k, v in a_dictionary.items() if v == value}
    for k in remove.keys():
        del a_dictionary[k]
    return (a_dictionary)
