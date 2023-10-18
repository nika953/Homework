arr = [6, 1, 6, 5, 8, 4]
for i in range(0, len(arr) - 1):
    if arr[i] > arr[i+1]:
        maxx = arr[i]
    else:
        maxx = arr[i+1]
    if arr[i] + arr[i+1] > arr[i+2]:
        print(arr[i])
        sums = arr[0] + arr[0+i] + arr[0+i+1]
        print(sums)
