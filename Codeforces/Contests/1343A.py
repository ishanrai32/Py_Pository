t = int(input())
for i in range(0, t):
    n = int(input())
    k = 2
    while k > 1:
        y = (2**k) - 1
        r = n % y

        if r == 0:
            break
        k = k + 1
    q = n // y
    print(q)

