def move1(h):
    a = h // 2 + 10
    return a


def move2(h):
    a = h - 10
    return a


t = int(input())
for i in range(0, t):
    x, n, m = [int(x) for x in input().split()]
    for j in range(0, n):
        if x <= 20:
            break
        x = move1(x)
    for k in range(0, m):
        x = move2(x)
    if x <= 0:
        print("YES")
    else:
        print("NO")
