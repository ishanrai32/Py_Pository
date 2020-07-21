k, n, w = [int(x) for x in input().split()]
s = w * (w + 1) * k
s = s // 2
if s > n:
    bor = s - n
    print(bor)
else:
    print("0")
