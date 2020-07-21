a = input()
b = input()
l1 = len(a)
l2 = len(b)
dp = [[0 for x in range(l1+1)] for y in range(l2+1)]

for i in range(l1+1):
    dp[0][i] = i
for j in range(l2+1):
    dp[j][0] = j

for i in range(1, l2+1):
    for j in range(1, l1+1):
        if a[j-1] == b[i-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
print(dp[l2][l1])

