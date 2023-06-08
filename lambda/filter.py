#!/usr/bin/python3
"""filter"""
nums = [1, 3, 9, 6, 4, 7, 8, 12, 17]
# Syntax for filter => filter(function, iterable)

#def odd_nums(n):
#if n % 2 != 0: 
 #       return n

#odds = list(filter(odd_nums, nums))
#print(odds)

#lambda n: n % 2 != 0
odds = list(filter(lambda n: n % 2 != 0, nums)) # return elements which are odd
print(odds) 


