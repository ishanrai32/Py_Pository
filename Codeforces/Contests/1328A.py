t = int(input())

for i in range(0, t):
    a, b = [int(x) for x in input().split()]
    if a % b == 0:
        n = 0
    else:
        r = a % b
        n = b - r
    print(n)
