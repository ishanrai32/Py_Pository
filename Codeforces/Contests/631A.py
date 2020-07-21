t = int(input())
for i in range(0, t):
    n, x = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    a.sort()
    for j in range(0, n-1):
        if a[j] == a[j+1]:
            del a[j+1]
    