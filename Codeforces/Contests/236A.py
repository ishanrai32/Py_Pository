a = list(input())
l = len(a)
b = []
b = b.append(a[0])
m = 1
flag = 1
for i in range(0, l):
    for j in range(0, m):
        if a[i] == b[j]:
            flag = 0
    if flag != 0:
        b = b.append(a[i])
        m = m + 1

print(b)
