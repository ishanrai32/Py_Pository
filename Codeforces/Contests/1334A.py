t = int(input())
for i in range(0, t):
    p1 = c1 = x = 0
    n = int(input())
    for j in range(0, n):
        p, c = [int(x) for x in input().split()]
        del_p = p - p1
        del_c = c - c1
        if (del_p >= 0) and (del_c >= 0) and (del_p >= del_c):
            x = x + 1
        p1 = p
        c1 = c
    if x == n:
        print("YES")
    else:
        print("NO")
