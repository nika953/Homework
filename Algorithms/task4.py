n = int(input())
count = 0
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        if i % 3 == 0:
            count += 1
        if i != (n // i) and (n // i) % 3 == 0:
            count += 1
print(count)