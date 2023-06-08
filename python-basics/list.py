#!/usr/bin/python3

def square():
    squares = []
    for i in range(0, 5): # 0, 1, 2, 3, 4
        if i == 3:
            continue
        squares.append(i**2)
    return squares

print(square())
print([i ** 2 for i in range(0, 5) if i != 3])

def square()
    return [i ** 2 for in range(0, 5) if i != 3]




