a, b = [int(x) for x in input().split()]
if b > a:
    temp = a
    a = b
    b = temp

while b > 0:
    x = a % b
    a = b
    b = x
print(a)
