import math

a = int(input())
x = [i for i in range(a)]

x.sort()
S = -1
maxS = -1

for i in range(2, a):

    if (x[i] < x[i - 2] + x[i - 1]):
        p = (x[i] + x[i - 1] + x[i - 2]) / 2
        S = math.sqrt(p * (p - x[i]) * (p - x[i - 1]) * (p - x[i - 2]))
        maxS = max(maxS, S)

print(maxS)