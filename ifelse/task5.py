number_1 = int(input("Введите число: "))
numbers = number_1
i = 0
while number_1 / 10:
    i = number_1 % 10 + i
    number_1 = number_1 // 10
if i % 3 == 0 and numbers % 2 == 0:
    print(i // 3)
    print(numbers, "Делиться на 6")



