#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    sum = 0
    for key, value in enumerate(argv):
        if key > 0:
            sum += int(value)
    print(sum)
