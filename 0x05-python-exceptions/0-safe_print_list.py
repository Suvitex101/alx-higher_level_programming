#!/usr/bin/python

def safe_print_list(my_list=[], x=0):
    """ function that prints x elements of a list."""
    tmp = 0
    for items in range(x):
        try:
            print("{}".format(my_list[items]), end="")
            tmp += 1
        except IndexError:
            break
    print("")
    return (tmp)
