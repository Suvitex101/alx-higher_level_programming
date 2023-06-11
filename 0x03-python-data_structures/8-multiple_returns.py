#!/usr/bin/python3

def multiple_returns(sentence):
    """function that returns a tuple
    with the length of a string and its first
    character"""

    new = ()
    if len(sentence) == 0:
        new = 0, "None"
    else:
        new = len(sentence), sentence[0]
    return new
