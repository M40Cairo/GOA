# Write a Python script that prints "Hello, World!"
print("Hello, World!")

# Create a script that takes user input and prints it.
user_input = input("Enter something: ")
print(user_input)

# Write a script that uses both single-line and multi-line comments.
'''
This is a 
multi-line comment
'''
print("123")

# Write a script that demonstrates indentation in Python.
if True:
    print("123")

# Write a script that shows how to break lines in Python.
long_string = "long string one " \
              "long string two " \
              "long string three. "
print(long_string)


'''________________________________________________________________'''

# Add comments to explain each line of a given script.
# This script takes user input and prints it.
user_input = input("Enter something: ")  # Take input from the user
print(user_input)  # Print the user's input

# Write a script and use comments to explain a function's purpose.
def hello(name):
    """
    This function takes a name as input
    and prints a greeting message.
    """
    print("Hello, {name}")
    
hello("Alice")

# Add a block comment to describe the script's overall functionality.
"""
this script demonstartes different tipes of comments
"""
print("comments")

# Use comments to disable a part of the script and re-enable it.
# print("disabled")
print("enabled")

# Write a script with intentional errors and comment on why they occur.
print("error"


result = "number: " + 5

#____________________________________________________________________________________________

# Create and initialize multiple variables of different data types.
integer = 10
float = 20.5
string = "Hello"
boolean = True

# Swap the values of two variables.
a = 5
b = 10
a, b = b, a  
print(a, b) 

# Create a script that takes user input to assign values to variables.
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Name: {name}, Age: {age}")

# Write a script that uses both global and local variables.
global = "global"

def function():
    local = "local"
    print(global)  
    print(local)

function()

# Demonstrate variable naming conventions in Python.
snake_case = "snake_case"
camelCase = "camelCase"
PascalCase = "PascalCase"

#____________________________________________________________________________

# Create variables of types: integer, float, string, and boolean.

integer = 32131
float = 904.12321
string = "saba"
boolean = True

# Demonstrate the use of type() function to check variable types.
print(type(integer))
print(type(float)) 
print(type(string))  
print(type(boolean))  

# Perform basic arithmetic operations on different data types.
sum_result = integer + float
mul_result = integer * float
print(sum_result, mul_result)

# Write a script to compare different data types using relational operators.
print(integer == float)  
print(integer > float)   

#_______________________________________________________________________________

# Write a script to perform arithmetic operations.
a = 10
b = 3
print(a + b) 
print(a - b)  
print(a * b)
print(a / b)  
print(a % b)  
print(a ** b) 

# Create a script that generates a random number.
import random
random_number = random.randint(0, 10000000000000)
print(random_number)

# Write a script that calculates the square root of a number.
import math
num = 30
sqrt = math.sqrt(num)
print(sqrt)

# Write a script to find the greatest common divisor (GCD) of two numbers.
num1 = 130
num2 = 400
gcd = math.gcd(num1, num2)
print(gcd)

#_______________________________________________________________________________

# Write a script to convert integers to floats and vice versa.
int = 10
float = float(int)
print(float)

float = 20.5
int = int(float)
print(int)

# Create a script to convert strings to integers and floats.
str = "123"
int = int(str)
float = float(str)
print(int, float)

# Demonstrate casting between lists and tuples.
list = [1, 2, 3]
tuple = tuple(list)
print(tuple)

tuple = (4, 5, 6)
list = list(tuple)
print(list)

# Write a script to handle casting errors.
str = "abc"
try:
    int = int(str)
except ValueError:
    print("cant convert")

# Create a script to convert a string representing a number to an integer.
str = "3213"
int = int(str)
print(int)

#___________________________________________________________________________________________
# Write a script to demonstrate the use of boolean values.
is_open = True
is_locked = False
print(f"is the door open? {is_open}")
print(f"is the door locked? {is_locked}")

# Create a script to perform logical operations (and, or, not).
is_night = True
is_daytime = False
print(f"is_night and is_daytime: {is_nightand is_daytime}") 
print(f"is_night or is_daytime: {is_night or is_daytime}")   
print(f"not is_night: {not is_night}")                        

# Demonstrate the use of comparison operators to return boolean values.
age = 15
height = 173
print(f"age == 18: {age == 18}")   
print(f"age != 18: {age != 18}")   
print(f"age > 15: {age > 15}")   
print(f"age < 20: {age < 20}")     
print(f"height >= 160: {height >= 160}"
print(f"height <= 150: {height <= 150}")  

# Write a script that uses if-else statements based on boolean values.
is_sunny = True
if is_sunny:
    print("get sunglasses")
else:
    print("dont take sunglasses")

# Create a script that returns a boolean result from a function.
def is_even(number):
    return number % 2 == 0

print(f"Is 4 even? {is_even(4)}")
print(f"Is 7 even? {is_even(7)}")  

#_____________________________________________________________________________

# Write a script that demonstrates arithmetic operators.
a = 20
b = 5
print(f"a + b = {a + b}")  
print(f"a - b = {a - b}") 
print(f"a * b = {a * b}")  
print(f"a / b = {a / b}")  
print(f"a % b = {a % b}")  
print(f"a ** b = {a ** b}") 

# Create a script to use assignment operators.
x = 10
x += 5
print(f"x += 5: {x}")
x -= 3
print(f"x -= 3: {x}")
x *= 2
print(f"x *= 2: {x}")
x /= 4
print(f"x /= 4: {x}")
x %= 3
print(f"x %= 3: {x}")
x **= 2
print(f"x **= 2: {x}")

# Write a script to show the use of comparison operators.
m = 7
n = 14
print(f"m == n: {m == n}")
print(f"m != n: {m != n}")
print(f"m > n: {m > n}")
print(f"m < n: {m < n}")
print(f"m >= 7: {m >= 7}")
print(f"n <= 10: {n <= 10}")

# Demonstrate the use of logical operators in a script.
is_adult = True
has_ticket = False
print(f"is_adult and has_ticket: {is_adult and has_ticket}")
print(f"is_adult or has_ticket: {is_adult or has_ticket}")
print(f"not has_ticket: {not has_ticket}")

# Create a script to use identity operators (is, is not).
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(f"x is y: {x is y}")  
print(f"x is z: {x is z}")  
print(f"x is not y: {x is not y}")  
print(f"x is not z: {x is not z}") 


#_______________________________________________________________________

# Write a script to create and print a list.
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Create a script to add and remove elements from a list.
fruits.append("orange")
print(fruits)
fruits.remove("banana")
print(fruits)

# Write a script to sort a list.
numbers = [3, 1, 4, 1, 5, 9]
numbers.sort()
print(numbers)

# Demonstrate the use of list comprehension.
squares = [x**2 for x in range(6)]
print(squares)

# Create a script to find the length of a list.
length_of_fruits = len(fruits)
print(f"Length of fruits list: {length_of_fruits}")

#_________________________________________________________________________

# Write a script that uses an if statement to check a condition.
age = 20
if age >= 18:
    print("You are an adult.")

# Create a script that uses an if-else statement.
temperature = 15
if temperature > 20:
    print("It's warm outside.")
else:
    print("It's cold outside.")

# Write a script that uses an if-elif-else statement.
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# Demonstrate nested if statements.
number = 10
if number > 0:
    if number % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
else:
    print("The number is not positive.")

# Write a script that uses the ternary operator.
age = 18
message = "Eligible to vote" if age >= 18 else "Not eligible to vote"
print(message)

#_____________________________________________________________________________

# Write a script to demonstrate a while loop.
count = 1
while count <= 5:
    print(count)
    count += 1

# Create a script that uses a while loop with a break statement.
n = 1
while n <= 10:
    if n == 5:
        break
    print(n)
    n += 1

# Write a script that uses a while loop with a continue statement.
m = 0
while m < 10:
    m += 1
    if m % 2 == 0:
        continue
    print(m)

# Demonstrate an infinite loop and how to stop it.
# ctrl+c to stop
# while True:
#     print("Infinite loop")

# Create a script that uses a while loop to iterate over a list.
colors = ["red", "green", "blue"]
index = 0
while index < len(colors):
    print(colors[index])
    index += 1

#_______________________________________________________________________________________________

# Write a script to demonstrate a for loop.
for i in range(5):
    print(i)

# Create a script that uses a for loop to iterate over a list.
animals = ["cat", "dog", "bird"]
for animal in animals:
    print(animal)

# Write a script that uses a for loop with the range() function.
for number in range(1, 10, 2):
    print(number)

# Demonstrate nested for loops.
for i in range(3):
    for j in range(3):
        print(f"i: {i}, j: {j}")

# Create a script that uses a for loop with an else clause.
for item in [1, 2, 3, 4]:
    print(item)
else:
    print("Loop is done")

#________________________________________________________________________________________

# Write a script to demonstrate a for loop.
for i in range(5):
    print(i)

# Create a script that uses a for loop to iterate over a list.
animals = ["cat", "dog", "bird"]
for animal in animals:
    print(animal)

# Write a script that uses a for loop with the range() function.
for number in range(1, 10, 2):
    print(number)

# Demonstrate nested for loops.
for i in range(3):
    for j in range(3):
        print(f"i: {i}, j: {j}")

# Create a script that uses a for loop with an else clause.
for item in [1, 2, 3, 4]:
    print(item)
else:
    print("Loop is done")

#_____________________________________________________________________________________________

# Write a script to define and call a function.
def greet():
    print("Hello, World!")

greet()

# Create a script that uses a function with parameters.
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")

# Write a script that uses a function with a return value.
def add(a, b):
    return a + b

result = add(3, 5)
print(f"Sum: {result}")

# Demonstrate the use of default parameters in a function.
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()
greet("Bob")

# Create a script that uses a function with keyword arguments.
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet(animal_type="dog", pet_name="Buddy")
describe_pet(pet_name="Whiskers", animal_type="cat")

#________________________________________________________________________________

