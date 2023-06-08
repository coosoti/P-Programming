#!/usr/bin/python3


#Syntax: map(function, iterable) #list, tuple

#def square_fn(n): #n is a list
#    return n ** 2

#range(1, 10, 2) # 1, 3, 5, 7, 9

#squares = map(square_fn, range(1, 10, 2) #return map object
#print(list(squares)) # [1, 9, 25, 49, 81


#square_fn = lambda n: n ** 2

square = list(map(lambda n: n ** 2, range(1, 10, 2))) 
print(square)


