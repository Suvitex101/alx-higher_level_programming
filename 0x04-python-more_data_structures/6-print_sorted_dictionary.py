#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """function that prints a dictionary by ordered keys"""
    lst = list(a_dictionary.keys())
    lst.sort()
    for i in lst:
        print("{}: {}".format(i, a_dictionary.get(i)))
