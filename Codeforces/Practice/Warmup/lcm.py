# LCM(a, b) * HCF(a, b) = a * b
a, b = [int(x) for x in input().split()]
prod = a * b
if b > a:
    temp = a
    a = b
    b = temp

while b > 0:
    x = a % b
    a = b
    b = x
lcm = prod // a
print(lcm)
