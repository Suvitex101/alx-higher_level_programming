#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """function that replaces an element in a list
    at a specific position
    without modifying the original list (like in C)"""

    if idx < 0 or idx > len(my_list) - 1:
        return my_list.copy()
    else:
        new = my_list.copy()
        my_list[idx] = element
        return new