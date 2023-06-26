#!/usr/bin/python3

def safe_print_division(a, b):
    """function that divides 2 integers and prints the result."""
    try:
        dv = a / b
    except (TypeError, ZeroDivisionError):
        dv = None
    finally:
        print("Inside result: {}".format(dv))
    return (dv)
