authorised = False
password = "123"

user_input = input("Enter your password: ")

if user_input == password:
    authorised = True
    print("Access granted")
else:
    while user_input != password:
        user_input = input("Incorrect password. Enter again: ")
    authorised = True
    print("Access granted")