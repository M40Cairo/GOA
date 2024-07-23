PIN = "4815"
authorized = False 

balance = "400$"

while authorized != True:
    user_input = input("please enter your password: ")

    if user_input == PIN:
         print("balance = " + balance)
         print(int(input("how much do you want to withdraw: ")))
         print(int(input("how much do you want to deposit: ")))
         authorized = True 
    else:
         print("PIN code is wrong, Please try again")