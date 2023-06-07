#!/usr/bin/python3

for i in range(122, 96, -1):
    """Function that prints the ASCII alphabet, in reverse order"""
    if i % 2 == 1:
        i = i - 32
    print("{:c}".format(i), end='')
