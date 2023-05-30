#!/usr/bin/python3
def print_ints_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (TypeError, ValueError):
            break
    print()
    return count

print_ints_list([1,2,3,4, "c", "charles", 9, 7], 8)
