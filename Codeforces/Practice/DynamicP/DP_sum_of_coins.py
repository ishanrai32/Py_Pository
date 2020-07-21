import math
s = int(input())  # Sum of coins that's needed
coins = [int(x) for x in input().split()]  # Denomination of coins available


def solve(x, coin):
    if x < 0:
        return math.inf
    if x == 0:
        return 0
    best = math.inf
    l = len(coin)
    for c in range(0, l):
        best = min(best, solve(x-(coin[c]))+1)
    return best


min_no = solve(s, coins)
print(min_no)