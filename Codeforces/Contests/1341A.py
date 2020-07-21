t = int(input())
for i in range(0, t):
    n, a, b, c, d = [int(x) for x in input().split()]
    min_grain = n * (a - b)
    max_grain = n * (a + b)
    min_sum = c - d
    max_sum = c + d
    if (min_grain <= min_sum) and (max_grain >= max_sum):
        x = 1
    elif (min_grain <= min_sum) and ((max_grain <= max_sum) and (max_grain >= min_sum)):
        x = 1
    elif ((min_grain >= min_sum) and (min_grain <= max_sum)) and (max_grain >= max_sum):
        x = 1
    elif (min_grain >= min_sum) and (max_grain <= max_sum):
        x = 1
    else:
        x = 0
    if x == 1:
        print("YES")
    else:
        print("NO")

