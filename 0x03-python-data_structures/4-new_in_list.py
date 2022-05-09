#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    l2 = my_list.copy()

    if 0 <= idx < len(my_list):
        l2[idx] = element

    return l2
