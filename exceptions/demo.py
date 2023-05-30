def safe_print_list(my_list=[], x=0):
    a = 0
    for i in range(x):
        print(my_list[i], end="")
        a += 1
    print("")
    return x


print(safe_print_list([0, 1, 2, 3, 4, 5, 6, 7], 10))

