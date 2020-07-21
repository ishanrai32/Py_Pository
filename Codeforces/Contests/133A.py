a = list(input())
n = len(a)
x = 0
for i in range(0, n):
    if a[i] == "H" or a[i] == "Q" or a[i] == "9":
        x = 1
if x == 1:
    print("YES")
else:
    print("NO")