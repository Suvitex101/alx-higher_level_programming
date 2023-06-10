#!/usr/bin/bash

def print_list_integer(my_list=[]):
    """Function to print interger"""
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
