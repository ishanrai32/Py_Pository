t = int(input())
for t in range(0, t):
    n, m = [int(x) for x in input().split()]
    x = 0
    if n == 1 or m == 1:
        x = 1
    if n == 2 and m == 2:
        x = 1
    if x == 1:
        print("YES")
    else:
        print("NO")