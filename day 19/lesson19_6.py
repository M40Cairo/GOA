# Given an array of integers, return a new array with each value doubled.

def double(a):
    list = []
    for i in a:
        list.append(i + i)
    
    print(list)

double([1, 2, 3])