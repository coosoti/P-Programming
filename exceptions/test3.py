#!/usr/bin/python3

def divide_numbers(y, x):
    if x == 0:
        raise ValueError("Cannot divide by zero")
    return y / x

def divide():
    try:
        result = divide_numbers(100, 0)
        print("Result: ", result)
    except ValueError as e:
        print("Error occurred: ", str(e))

divide()


