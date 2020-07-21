t = int(input())
for i in range(0, t):
    a = ""
    b = ""
    n = int(input())
    x = list(input())
    z = 1
    for k in range(0, n):
        if x[k] == "0":
            a = a + "0"
            b = b + "0"
        elif x[k] == "1":
            a = a + "1"
            b = b + "0"
            break
        else:
            a = a + "1"
            b = b + "1"
        z = z + 1
    if z == n:
        print(a)
        print(b)
    else:
        for m in range(z, n):
            a = a + "0"
            b = b + x[m]
        print(a)
        print(b)

