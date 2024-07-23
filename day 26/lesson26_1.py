# 1. Manual Sum Function: Create a function called manual_sum 
# that iterates over list and adds their sum in a variable, then returns 
# variable. Use for loop for this task.


def manual_sum(a):
    list = []
    for i in a:
        list.append(sum(a))
    print(list)


manual_sum([1, 2, 3, 4])

   
