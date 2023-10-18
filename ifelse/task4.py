category = input("Введите категорию: ")
if category == ("Продукты"):
    sums = int(input("Введите цену: "))
    if sums < 100:
        print("Попробуйте нашу выпечку")
    elif 100 <= sums and sums < 500:
        print("Как насчёт орехов в шоколаде?")
    else:
        print("Попробуйте экзотические фрукты!")
else:
    print("Загляните в товары для дома!")