t = int(input())
for i in range(0, t):
    x, y = [int(x) for x in input().split()]
    a, b = [int(x) for x in input().split()]
    x = abs(x)
    y = abs(y)
    b_count = min(x, y)
    x1 = x - b_count
    y1 = y - b_count
    if x1 == 0:
        a_count = y1
    else:
        a_count = x1
    cost1 = (a * a_count) + (b * b_count)
    cost2 = a * (x + y)
    cost = min(cost1, cost2)
    print(cost)

