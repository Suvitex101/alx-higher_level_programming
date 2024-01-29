#!/usr/bin/python3

"""Python inheritance"""


class MyList(list):
    """Class to print sorted list"""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
