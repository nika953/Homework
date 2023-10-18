weight = int(input("Введите массу в кг: "))
height = int(input("Введите рост в см: "))
I = weight / ((height/ 100) ** 2)
print(round(I, 2))