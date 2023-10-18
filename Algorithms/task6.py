# import numpy as np
#
# a = np.zeros((5,5))
# a[4:5, 0:3] += 1
# print(a)

n = 6
def printMatrix(a):
    for s in a:
        print(s)

a = [[0] * n for _ in range(n)]
printMatrix(a)

q = [4, 0, 5, 3]

a[q[0]:q[2] + 1 ]