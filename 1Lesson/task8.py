number = int(input("Введите трехзначное число: "))
number_1 = number // 100
number_2 = number // 10 % 10
number_3 = number % 10
print(number_1 + number_2 + number_3)