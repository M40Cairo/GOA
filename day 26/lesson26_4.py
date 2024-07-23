# 4. Manual Len Function: Develop a function named manual_len 
# that iterates through list, counting each element, and returns 
# the count as the length of the list. Use for loop for this task.


def manual_len(a):
    list = []
    for i in a:
        list.append(len(a))
    
    print(list)


manual_len([3, 2, 3, 2, 3, 2, 3, 2])

