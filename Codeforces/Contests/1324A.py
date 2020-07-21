t = int(input())
for t in range(0, t):
    n = int(input())
    a = [int(x) for x in input().split()]
    x = 0
    for i in range(0, n-1):
        d = a[i+1] - a[i]
        if d % 2 == 0:
            x = x + 1
    if x == n-1:
        print("YES")
    else:
        print("NO")
