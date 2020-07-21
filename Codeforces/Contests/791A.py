a, b = [int(x) for x in input().split()]
yrs = 0
while a <= b:
    a = a * 3
    b = b * 2
    yrs = yrs + 1
print(yrs)
