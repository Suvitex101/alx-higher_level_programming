#!/usr/bin/python3

def number_keys(a_dictionary):
    """function that returns the number of keys in a dictionary"""
    n = 0
    l_keys = list(a_dictionary.keys())

    for i in l_keys:
        n += 1

    return (n)
