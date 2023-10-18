# mark = list(input("Введите оценки через пробел: ").split(" "))
# A = 0
# B = 0
# C = 0
# for item in mark:
#     if item == "5":
#         A += 1
# print(A)
# for item in mark:
#     if item == "4":
#         B += 1
# print(B)
# for item in mark:
#     if item == "3":
#         C += 1
# print(C)
# print(sorted(mark))
# print()
# print((A + B + C) / len(mark) * 100)

mark = list(input("Введите оценки через пробел: ").split(" "))
print(sorted(mark))
print((mark.count("5") + mark.count("4") + mark.count("3")) / len(mark) * 100)
