def get_count(sentence):
    count = 0
    
    for i in sentence:
        if i == 'a':
            count += 1
        elif i == 'e':
            count += 1
        elif i == 'i':
            count += 1
        elif i == 'o':
            count +=1
        elif i == 'u':
            coun += 1
    return count   

get_count(['nika', 'sandro', 'luka'])