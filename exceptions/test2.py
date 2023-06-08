#!/usr/bin/python3
"""function takes two number and divide them"""
def divide():
    try:
        x = int(input("Enter the value of x: "))
        y = int(input("Enter the value of y: "))
        result = x / y
        print(result)

    except ValueError:
        print("Invalid input. Enter another number. ")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        print("Code executed successfully")

divide()
