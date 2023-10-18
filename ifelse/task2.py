times = int(input("Введите время: "))
sums = int(input("Введите сумму: "))
if times <= 12 and times >= 10:
    print(sums / 2)
elif times <= 22 and times >= 20:
    print(sums / 4)
elif times < 8 or times > 22:
    print("Магазин закрыт")
else:
    print(sums)