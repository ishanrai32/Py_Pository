s = input()
l = len(s)
a = "hello"
x = 0
for i in range(0, l):
    if s[i] == a[x]:
        x = x + 1
    if x == 5:
        break
if x == 5:
    print("YES")
else:
    print("NO")

