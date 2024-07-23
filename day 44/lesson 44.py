def solution(s):
    # initialize an empty list to store the pairs
    split_list = []

    # if the length of the string is odd, append an underscore to make it even
    if len(s) % 2 != 0:
        s += "_"

    # iterate over the string in steps of 2
    for i in range(0, len(s), 2):
        # form a pair by combining the current character and the next character
        pair = s[i] + s[i + 1]
        # append the pair to the split_list
        split_list.append(pair)
    
    # return the list of pairs
    return split_list