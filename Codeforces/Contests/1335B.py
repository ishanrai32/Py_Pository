t = int(input())
for i in range(0, t):
    n, a, b = [int(x) for x in input().split()]
    # number of repeated characters
    c = a - b
    x = []
    for j in range(0, b):
        x.append(int(j))
    for k in range(0, c):
        x.append(x[0])
    q = n // a
    r = n % a
    x = x * q
    for l in range(0, r):
        x.append(x[l])

    # finally convert them to letters
    for m in range(0, n):
        x[m] = x[m] + ord('a')
        x[m] = chr(x[m])

    # We need a string
    y = ""
    for o in range(0, n):
        y = y + x[o]
    print(y)