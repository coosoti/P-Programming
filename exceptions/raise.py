def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def divide():
    try:
        result = divide_numbers(10, 0)
        print("Result:", result)
    except ValueError as e:
        print("An error occurred:", str(e))

divide()
