t = int(input())
for t in range(t):
    r, g, b = [int(x) for x in input().split()]
    if g == max(r, g, b):
        temp = r
        r = g
        g = temp
    elif b == max(r, g, b):
        temp = r
        r = b
        b = temp

    if r >= g + b:
        x = g + b
    else:
        x = (r + g + b) // 2
    print(x)
