t = int(input())
for i in range(0, t):
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    a = [str(x) for x in a]
    if n % 2 == 0:
        x = []
        for j in range(0, n // 2):
            x.append(a[0])
            del a[0]
        y = []
        x.reverse()
        for k in range(0, n // 2):
            y.append(x[k])
            y.append(a[k])
    else:
        x = []
        for j in range(0, n // 2):
            x.append(a[0])
            del a[0]
        y = []
        x.reverse()
        y.append(a[0])
        del a[0]
        for k in range(0, n // 2):
            y.append(x[k])
            y.append(a[k])
    print(*y)