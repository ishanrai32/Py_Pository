def count(S, m, n):
    dp = [[0 for x in range(n + 1)] for x in range(m)]
    # making an empty matrix for dp, we will have n+1 columns as base
    # case of target value 0 has to be included and m rows for each
    # denomination

    # now first complete base case i.e. n = 0
    for i in range(n+1):
        dp[0][i] = i

    # filling the rest of the matrix in bottom-up approach
    for i in range(1, m):
        for j in range(1, n + 1):
            if j >= S[i]:
                dp[i][j] = min(dp[i - 1][j], 1 + dp[i][j - S[i]])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[m-1][n]


n = int(input())
S = [1, 3, 4]
m = 3
print(count(S, m, n))
