operators = ('+, =, *, /')
num1 = int(input('enter first number: '))
num2 = int(input('enter second number: '))
choose_operator = input('''choose 1 operator from the list: 
+
-
*
/
chosen operator: ''')

if choose_operator == '+':
    print(num1 + num2)
elif choose_operator == '-':
    print(num1 - num2)
elif choose_operator == ('*'):
    print(num1 * num2)
elif choose_operator == ('/'):
    print(num1 / num2)