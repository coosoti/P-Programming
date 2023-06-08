#!/usr/bin/python3
"""This module contains functions"""
def add(a, b):
    """this function adds two integers

    Args:
        a (int): first argument passed to the function
        b (int): second argument passed to the function
    Returns:
        sum of the two numbers

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or a float")
    return int(a) + int(b)

def multiply(a, b):
    """multiplies two integers
    """

