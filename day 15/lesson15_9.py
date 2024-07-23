user_input = int(input('enter your number: '))

list = []

for i in range(0, user_input):
    if i %2 == 0:
        list.append(i)

print(list)