W, n = [int(x) for x in input().split()]
w = [int(x) for x in input().split()]

dp = [[0 for x in range(W+1)] for y in range(n+1)]

for i in range(1, n+1):
    for j in range(1, W+1):
        # checking if the weight is less/equal than/to W
        if w[i-1] <= j:
            dp[i][j] = max(w[i-1] + dp[i-1][j - w[i-1]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][W])
