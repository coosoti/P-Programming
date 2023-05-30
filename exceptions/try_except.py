def divide():
    try:
        x = int(input("Enter x number: "))
        y = int(input("Enter y number: "))
        result = x / y
        print("Result:", result)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")


divide()
