# mark = list(input("Введите оценки через пробел: ").split(" "))
# A = 0
# for item in mark:
#     if item == "5":
#         A += 1
#     print(A)
# print(A / len(mark) * 100)

mark = list(input("Введите оценки через пробел: ").split(" "))
print(mark.count("5") / len(mark) * 100)