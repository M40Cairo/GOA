# Create a function that returns the sum of the two lowest positive 
# numbers given an array of minimum 4 positive integers. No floats or 
# non-positive integers will be passed.

def sum_two_smallest_numbers(numbers):
    low1 = numbers[0]
    low2 = numbers[1]
    for num in numbers[1:]:
        if num < low1:
            low2 = low1
            low1 = num
        elif num < low2 and num != low1:
            low2 = num
    return low1 + low2

sum_two_smallest_numbers([2, 34, 5, 1])