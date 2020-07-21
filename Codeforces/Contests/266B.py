n, t = [int(x) for x in input().split()]
s = list(input())
for i in range(0, t):
    j = 0
    while j < n-1:
        if s[j] == "B" and s[j+1] == "G":
            temp = s[j]
            s[j] = s[j+1]
            s[j+1] = temp
            j = j + 2
        else:
            j = j + 1

a = ""
for k in range(0, n):
    a = a + s[k]
print(a)
