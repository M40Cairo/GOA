# Given a non-empty array of integers, return the result of multiplying the values together in order.

def multiply(a):
    list = []
    for i in a:
        i = i * i
        list.append(i + i)
    
    print(list)

multiply([1, 2, 3, 4])