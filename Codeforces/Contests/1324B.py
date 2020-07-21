t = int(input())
for t in range(0, t):
    n = int(input())
    a = [int(x) for x in input().split()]
    x = 0
    for i in range(0, n-2):
        for j in range(i+2, n):
            if a[i] == a[j]:
                x = 1
                break
        if x == 1:
            break
    if x == 1:
        print("YES")
    else:
        print("NO")