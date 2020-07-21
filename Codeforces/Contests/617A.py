x = int(input())
q = x // 5
r = x % 5
if r == 0:
    print(q)
else:
    q = q + 1
    print(q)