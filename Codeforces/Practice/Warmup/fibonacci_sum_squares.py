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

n = n % period
a = F[n]

m = (n + 1) % period
b = F[m]

c = a * b
print(c % 10)
