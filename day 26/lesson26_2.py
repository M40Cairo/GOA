# 2. Manual Max Function: Define a function 
# named manual_max that iterates through list, 
# updating a variable with the maximum value, then returns
#  the maximum value found. Use for loop for this task.

def manual_max(a):
    list = []
    for i in a:
        list.append(max(a))
    
    print(list)


manual_max([1, 2, 4, 3])

