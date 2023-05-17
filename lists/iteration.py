def sum_of_elements(my_list):
    total = 0
    for i in range(len(my_list)):
        total += my_list[i]
    return total

print(sum_of_elements([1,2,3,4,5,6]))
