#!/usr/bin/python3
def print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(my_list[i], end="")
    except IndexError:
        print("")


my_list = [0,1,2,3,4]

print_list(my_list, 10)
