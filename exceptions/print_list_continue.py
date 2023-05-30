#!/usr/bin/python3
def print_all_integers_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (TypeError, ValueError):
            continue
    print()
    return count

print_all_integers_list([1,2,3,4, "c", "charles", 9, 7], 8)
