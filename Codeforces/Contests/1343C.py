def sign(z):
    if int(z) > 0:
        return 1
    else:
        return 0


t = int(input())
for t in range(0, t):
    n = int(input())
    a = [int(x) for x in input().split()]
    x = 0
    i = 0
    while i < n:
        j = i
        mx = a[j]

        while (j < n) and (sign(a[j]) == sign(a[i])):
            mx = max(a[j], mx)
            j = j + 1
        i = j - 1
        x = x + mx
        i = i + 1
    print(x)
