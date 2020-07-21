n = int(input())
a = []
b = []
x = 1
for n in range(0, n):
    a_i, b_i = [int(x) for x in input().split()]
    a.append(a_i)
    b.append(b_i)
index = list(range(n))
index.sort(key=lambda i: b[i])
for i in index:
    if i == n:
        continue
    if a[i+1] == a[i]:
        if

