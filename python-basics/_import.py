#!/usr/bin/python3

from sys import argv
from calculator import add, sub, mul, div

if __name__ == '__main__':
    num_of_args = len(argv[1:])
    args = argv[1:]

    if num_of_args != 3:
        print("Usage: ./_import.py <a> <operator> <b>")
        exit(1)
    if num_of_args == 3:
        a = int(args[0])
        b = int(args[2])
        op = args[1]
        if args[1] == '+':
            print("{} + {} = {}".format(a, b, add(a, b)))
        if args[1] == '-':
            print("{} - {} = {}".format(a, b, sub(a, b)))
        if args[1] == "*":
            print("{} * {} = {}".format(a, b, mul(a, b)))
        if args[1] == '/':
            print("{} / {} = {}".format(a, b, div(a, b)))
        elif(op != '+' and op != '-' and op != '*' and op != '/'):
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)


