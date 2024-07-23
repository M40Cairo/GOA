# ექმენით ფუნქცია, რომელსაც გადასცემთ მომხმარებლის გვარს.
# გვარის თითოეული ასო გადაიტანეთ ახალ სიაში. 
# შემდეგ for ციკლის გამოყენებით იმუშავეთ ამ სიაზე 
# - მარტო ლუწ ინდექსებზე მყოფი ასოები დაამატეთ ახალ სიაში. საბოლოოდ დააბრუნეთ ეს სია.


def lastname(surname):
    list1 = []
    list2 = []

    for i in surname:
         list1.append(i)

    for i in list1:
         if list1.index(i) %2 == 0:
            list2.append(i)
         else:
            pass
    print(list2)

lastname('shavela')