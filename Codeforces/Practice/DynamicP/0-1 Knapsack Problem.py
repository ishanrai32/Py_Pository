# Given weights and values of a list of items, pick items to put in a Knapsack of specified weight capacity such that
# no item is fractional or picked more than once and the value is maximized

W = int(input("Enter the Weight capacity of Knapsack"))
print("Enter the List of weights of items")
wt = [int(x) for x in input().split()]
print("Enter the List of values of items")
val = [int(x) for x in input().split()]

# Number of items
n = len(wt)

dp = [[0 for x in range(W+1)] for y in range(n+1)]

for i in range(1, n+1):
    for j in range(1, W+1):
        if j < wt[i-1]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], val[i-1] + dp[i-1][j - wt[i-1]])
print(dp[n][W])
