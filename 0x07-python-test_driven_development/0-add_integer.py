#!/usr/bin/python3
"""This module contains a function that adds 2 integers"""

def add_integer(a, b=98):
    """This function adds two numbers

    Examples:
        >>> add_integer(4, 2)
        6
        >>> add_integer(4.0, 2.0)
        6

    Args:
        a (int): first argument passed
        b (int, optional): second argument passed, if not passed then optional

    Returns:
        sum of a and b

    Raises:
        TypeError:  An error
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
