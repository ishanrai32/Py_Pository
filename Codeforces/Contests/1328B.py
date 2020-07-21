t = int(input())
for i in range(0, t):
    n, k = [int(x) for x in input().split()]
    index_first_b = -2
    for j in range(1, n):
        Sn = (j * (j+1)) // 2
        if Sn >= k:
            break
        index_first_b = index_first_b - 1
    index_first_b = index_first_b + n
    index_gap = Sn - k
    index_sec_b = index_first_b + index_gap + 1
    x = []
    for k in range(0, n):
        x.append("a")
    x[index_first_b] = "b"
    x[index_sec_b] = "b"
    print(*x, sep="")

