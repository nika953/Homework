N = int(input())
Arr = list(input().split(","))
Arr = [int(i) for i in Arr]
S = N * (1 + N) / 2
for i in Arr:
    S -= i
print(int(S))