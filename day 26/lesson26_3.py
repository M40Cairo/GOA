# 3. Manual Min Function: Define a function named 
# manual_min that iterates through list, updating a variable 
# with the minimum value, then returns the minimum value found. 
# Use for loop for this task.

def manual_min(a):
    list = []
    for i in a:
        list.append(min(a))

    print(list)


manual_min([5, 2, 3, 4])