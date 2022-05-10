#!/usr/bin/python3
def roman_to_int(roman_string):

    if (type(roman_string) is str):

        number = list(roman_string)
        romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                  'M': 1000}
        sum = 0

        for i in number:
            for k, v in romans.items():
                if (i == k):
                    sum += v
        return sum
    else:
        return (0)

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))