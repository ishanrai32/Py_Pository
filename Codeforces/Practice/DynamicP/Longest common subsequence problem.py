a = input("Enter the first string")
b = input("Enter the second string")
x = len(a)
y = len(b)

dp = [[0 for x in range(x+1)] for y in range(y+1)]

for i in range(1, y+1):
    for j in range(1, x+1):
        if a[j-1] == b[i-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[y][x])