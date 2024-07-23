num = int(input('enter a number: '))

factorial = 1 

if num < 0:
    print('cant be < 0')
elif num == 0:
    print('its 1')
else:
    for i in range(1,num + 1):
        factorial = factorial*i
    print('the factorial of',num,'is',factorial)