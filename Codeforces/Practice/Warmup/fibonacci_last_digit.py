import math
n = int(input())
a = 0
b = 1
x = [a,b]
for i in range(0, math.ceil(n/2) + 1):
    a = (a + b) % 10
    b = (b + a) % 10
    x.append(a)
    x.append(b)
print(x[n])
