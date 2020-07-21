import math
n = int(input())
a = input().split()
a = [int(i) for i in a]
count = 0
ones = twos = threes = 0
for j in range(0, n):
    if a[j] == 4:
        count = count + 1
    elif a[j] == 3:
        threes = threes + 1
    elif a[j] == 2:
        twos = twos + 1
    else:
        ones = ones + 1
count = count + threes
if ones <= threes:
    ones = 0
else:
    ones = ones - threes
ot = ones + (twos * 2)
ot = ot / 4
ot = math.ceil(ot)
count = count + int(ot)
print(count)
