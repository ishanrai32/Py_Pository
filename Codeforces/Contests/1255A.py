t = int(input())
for t in range(0, t):
    a, b = [int(x) for x in input().split()]
    dif = abs(a - b)
    x = dif // 5
    r = dif % 5
    y = r // 2
    r = r % 2
    print(x + y + r)
