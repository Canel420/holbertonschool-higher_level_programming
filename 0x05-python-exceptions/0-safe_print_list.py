#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    while count < x:
        try:
            elm = my_list[count]
            count += 1
            print(elm, end="")
        except IndexError:
            break
    print("")
    return (count)
