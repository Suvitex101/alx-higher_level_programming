#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """function that prints a matrix of integers"""
    for i in matrix:
        for element in i:
            if element != i[-1]:
                print("{:d}".format(element), end=" ")
            else:
                print("{:d}".format(element), end="")
        print()
