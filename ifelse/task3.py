product_1 = int(input())
product_2 = int(input())
product_3 = int(input())
sums = sum([product_1, product_2, product_3])
if product_1 < product_2 < product_3:
    print("Акция!", sums/2)
elif product_3 < product_2 and product_2 < product_1:
    print("Акция!", sums/3)
else:
    print("К оплате:", sums)