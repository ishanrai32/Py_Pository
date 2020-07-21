t = int(input())
for i in range(0, t):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    a.reverse()
    b.reverse()
    for j in range(0, n):
        if a[j] == b[j]:
            x = 1
        elif a[j] < b[j]:
            for k in range(j+1, n):
                if a[k] == 1:
                    x = 1
                else:
                    x = 0
        else:
            for k in range(j+1, n):
                if a[k] == -1:
                    x = 1
                else:
                    x = 0
    if x == 1:
        print("YES")
    else:
        print("NO")

