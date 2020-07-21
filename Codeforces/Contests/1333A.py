t = int(input())
for i in range(0, t):
    n, m = [int(x) for x in input().split()]
    for j in range(0, n):
        a = ""
        for k in range(0, m):
            if k == 0 and j == 0:
                a = a + "W"
            else:
                a = a + "B"
        print(a)
