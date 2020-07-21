t = int(input())
for t in range(0, t):
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    if n > m:
        print(-1)
    elif n == 2:
        print(-1)
    else:
        print(2 * sum(a))
        for i in range(1, n+1):
            x = i + 1
            if i == n:
                x = 1
            print(i, x)
