user_password = input('please enter your password: ')

password = 'Goa Best'

count = 1
while user_password != password:
    user_password = input('please enter your password: ')
    count += 1
    print(count)
if user_password == password:
    print('password correct')
    print('it took you ' + str(count) + ' tries')