#!/usr/bin/python3
"""matrix_divided function for a TDD project."""


def matrix_divided(matrix, div):
    '''Divides all elements of a matrix.
    Args:
        matrix (list): The matrix whose elements are to be divided.
        div (int): The number to use as a divisor.
    Returns:
        list: A new list consiting of the result of dividing each element
        in the given matrix by div.
    '''
    msg = (
        'matrix must be a matrix (list of lists) of integers/floats',
        'Each row of the matrix must have the same size',
        'div must be a number',
        'division by zero'
    )
    size = [0, 0]
    tep = []
    if not isinstance(matrix, list):
        raise TypeError(msg[0])
    size[0] = len(matrix)
    if size[0] == 0:
        raise TypeError(msg[0])
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(msg[0])
        elif len(row) == 0:
            raise TypeError(msg[0])
        else:
            if size[1] == 0:
                size[1] = len(row)
            elif len(row) != size[1]:
                raise TypeError(msg[1])
            for col in row:
                if not isinstance(col, (int, float)):
                    raise TypeError(msg[0])
    if not isinstance(div, (int, float)):
        raise TypeError(msg[2])
    elif div == 0:
        raise ZeroDivisionError(msg[3])
    else:
        for row in matrix:
            tep_row = list(map(lambda x: round(x / div, 2), row))
            tep.append(tep_row)
        return tep
