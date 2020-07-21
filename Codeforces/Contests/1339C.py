t = int(input())
for i in range(0, t):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in a]
    for j in range(0, n-1):
        if b[j] > b[j+1]:
            b[j+1] = b[j]
    x = 0
    for k in range(0, n):
        c = b[k] - a[k]
        x = max(c, x)
    s = 0
    p = 0
    while s < x:
        s = 2**p + s
        p = p + 1
    print(p)





