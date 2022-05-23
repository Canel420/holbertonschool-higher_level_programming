#!/usr/bin/python3
def safe_print_integer(value):
    try:
        val = int(value)
    except ValueError:
        return False
    else:
        print("{:d}".format(val))
        return True
