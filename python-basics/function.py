#!/usr/bin/python3

"""
Write a program that prints the maximum value of all the variable number of argumets

"""

def maximum(*args):

    if len(args) == 0:
        return None
    else:
        max_value = args[0]
        for arg in args[1:]:         
            if arg > max_value:
                max_value = arg
        return max_value

print(maximum())
print(maximum(2, 9, -100)) #return 9
print(maximum(123, 34536, 466747, 4677)) # return 466747

### [10, 4, 20, 7, 1]  => list in variables

args[0] 10 => max_value
args[1] 4 index 1 => 10  #for loop iteration 
args[2] 20 next => max_value => 20
args[3] 7 max_value => 20
args[4] 1 max_value => 20



