width = float(input("Ширина поверхности в м: "))
heigth = float(input("Высота поверхности м: "))
flow = int(input("Расход краски кв.м/л: "))
volume = int(input("Объем банки в литрах: "))
percent = int(input("Процент запаса: "))
area = width * heigth
liters = area / flow * (100 + percent) / 100
banks = round(liters / volume) + 1
left = volume * banks - liters 
print(round(area, 2))
print(round(liters, 2))
print(banks)
print(round(left, 2))