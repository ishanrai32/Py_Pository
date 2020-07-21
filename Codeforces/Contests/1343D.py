t = int(input())
for t in range(0, t):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    mn = n
    for x in range(2, (2*k + 1)):  # Iterating through all possible x, and storing the min moves "x" in every iteration
        p = q = r = 0
        for i in range(0, n // 2):  # Two pointer algo
            j = -1 - i
            if a[i] + a[j] == x:  # condition for 0 moves
                p = p + 1
            elif (min(a[i], a[j]) + 1 > x) or (max(a[i], a[j]) + k < x):  # condition for 2 moves being needed
                q = q + 1
            else:
                r = r + 1  # Remaining need 1 move
        moves = 0 * p + 1 * r + 2 * q
        mn = min(mn, moves)
    print(mn)




