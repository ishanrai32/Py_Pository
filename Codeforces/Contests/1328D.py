q = int(input())
for i in range(0, q):
    n = int(input())
    t = [int(x) for x in input().split()]
    t.append(t[0])
    x = 0
    c = []
    for j in range(0, n):
        if t[j] != t[j+1]:
            x = x + 1
        if t[j] == t[j+1]:
            break
    if x == 0:
        k = 1
        for k in range(0, n):
            c.append(1)
    elif x == n:
        if n % 2 == 0:
            k = 2
            for l in range(0, n // 2):
                c.append(1)
                c.append(2)
        else:
            k = 3
            for m in range(0, n // 2):
                c.append(1)
                c.append(2)
            c.append(3)
    else:
        if n % 2 == 0:
            k = 2
            for m in range(0, n // 2):
                c.append(1)
                c.append(2)
        else:
            k = 2
            if x % 2 == 0:
                for m in range(0, x // 2):
                    c.append(1)
                    c.append(2)
                c.append(1)
                c.append(1)
                for o in range(x+2, n // 2):
                    c.append(2)
                    c.append(1)
                c.append(2)
            else:
                for m in range(0, x // 2):
                    c.append(1)
                    c.append(2)
                c.append(1)
                c.append(2)
                c.append(2)
                for o in range(x+2, n // 2):
                    c.append(1)
                    c.append(2)
    k = max(c)
    print(k)
    print(*c)








