n, m = [int(x) for x in input().split()]
x = 0
y = 1
z = 0
F = [x, y]
while z != 1:
    x = (x + y) % m
    y = (x + y) % m
    if x == 0 and y == 1:
        z = 1
        break
    F.append(x)
    F.append(y)

period = len(F)
if m == 2:
    period = period // 2

n = n % period
a = F[n]
print(a)


