def sum(nums):
    list = []
    
    n = 0
    for i in nums:
        n += i
        list.append(n)
    print(list)
    

sum([1, 5.2, 4, 0, -1])