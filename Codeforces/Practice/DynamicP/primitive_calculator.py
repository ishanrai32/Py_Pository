n = int(input())
count = [0] * (n + 1)
count[0] = -1
count[1] = 0
if n >= 2:
    count[2] = 1
if n >= 3:
    count[3] = 1

for i in range(4, n + 1):
    if i % 2 == 0:
        count[i] = count[i // 2] + 1
    else:
        if i % 3 == 0:
            count[i] = count[i // 3] + 1
        else:
            count[i] = count[i - 1] + 1
x = count[n]
print(x)

array = [n]
while n > 1:
    if n % 2 == 0:
        array.append(n // 2)
        n = n // 2
    else:
        if n % 3 == 0:
            array.append(n//3)
            n = n // 3
        else:
            array.append(n-1)
            n = n - 1
array.sort()
print(*array)
