def divideZero(num):
    try:
        return num // 0
    except ZeroDivisionError:
        raise ValueError("num cannot be divided by zero")

print(divideZero(100))
