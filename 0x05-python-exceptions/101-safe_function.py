#!/usr/bin/python3
import sys
from __future__ import print_function
def safe_function(fct, *args):
    """function that executes a function safely."""
    try:
        tmp = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
    else:
        return tmp
