n = int(input())
a = n // 100
r = n % 100
b = r // 20
r = r % 20
c = r // 10
r = r % 10
d = r // 5
r = r % 5
x = a + b + c + d + r
print(x)