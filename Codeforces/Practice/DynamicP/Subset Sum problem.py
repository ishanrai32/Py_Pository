# Find out if it's possible to have a subset of the array who's sum is s
s = int(input("Enter the sum required"))
print("Enter the array")
a = [int(x) for x in input().split()]
n = len(a)

dp = [[0 for x in range(s+1)] for y in range(n+1)]

for i in range(n+1):
    dp[i][0] = 1

for i in range(1, n+1):
    for j in range(1, s+1):
        if j < a[i-1]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - a[i-1]])
print(dp[n][s])
