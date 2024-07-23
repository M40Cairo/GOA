def find_last_even(numbers_list):
#შემოვიტანეთ ფუნქცია 
    for i in range(len(numbers_list) - 1, -1, -1):
#შემდეგ i-ს დახმარებით ვამოწმებთ სიას
        if numbers_list[i] % 2 == 0:
            return numbers_list[i]
#ვეუბნებით პროგრამას, თუ i ჰაყოფილი 2-ზე არის 0-ის ტოლი, დაგვიბრუნოს სია
print(find_last_even([1,2,3,4,5]))

