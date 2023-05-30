#!/usr/bin/python3
def print_integer():
    try:
        value = int(input("Enter a value: "))
        print("{:d}".format(value))
    except (ValueError, TypeError):
        return False
    else:
        return True

print_integer()
