t = int(input())
for i in range(0, t):
    n = int(input())
    q = n // 2
    r = q % 2
    if r == 0:
        a = []
        for j in range(0, n // 2):
            x = 2 * (j+1)
            a.append(x)
        for k in range(0, n // 2):
            y = (2 * (k)) + 1
            a.append(y)
        a[n-1] = a[n-1] + n // 2
        print("YES")
        print(*a)
    else:
        print("NO")