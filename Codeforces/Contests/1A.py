import math
n, m, a = [int(x) for x in input().split()]

qn = n / a
qm = m / a
x = math.ceil(qn)
y = math.ceil(qm)
print(x * y)
