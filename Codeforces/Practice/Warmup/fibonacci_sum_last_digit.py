n = int(input())
x = 0
y = 1
z = 0
F = [x, y]
while z != 1:
    x = (x + y) % 10
    y = (x + y) % 10
    if x == 0 and y == 1:
        z = 1
        break
    F.append(x)
    F.append(y)

period = len(F)

n = (n + 2) % period
a = F[n] - 1
if a < 0:
    a = a + 10
print(a)