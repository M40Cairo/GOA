def smaller(arr): # We created a function called smaller and assigned the attribute arr
    result = [] # We created a variable called result and assigned it the value: an empty list
    count = 0 # We created a variable called count and assigned it the value 0
    for i in range(len(arr)): # We used a for loop to repeat a specific action as many times as the length of the list, to avoid going out of bounds
        # The len function calculates the length of the list.
        for j in range(i + 1, len(arr)): # We nested another for loop inside the first for loop, starting from i + 1 because i cannot work. The end is the length of the list.
            if arr[i] > arr[j]: # If the character at the next index in the list is greater than the previous one, then the count variable will be incremented by 1.
                count += 1
        result.append(count) # Then we return to the first for loop. The obtained result in count is added to the result variable, and then count becomes 0
        count = 0
    return result # Finally, we return the resulting list.
