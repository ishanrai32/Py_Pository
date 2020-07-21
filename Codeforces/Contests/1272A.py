t = int(input())
for t in range(0, t):
    x = [int(x) for x in input().split()]
    x.sort(reverse=True)
    a, b, c = [int(x) for x in x]
    d = a - c
    if d < 2:
        print(0)
    else:
        print(2 * (d - 2))
