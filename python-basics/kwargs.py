#!/usr/bin/python3

def user_details(**kwargs):
    """
    docstring
    """
    for key, value in kwargs.items():
        print(f"{key}: {value}")

user_details(first_name="Charles", last_name="Victor")
