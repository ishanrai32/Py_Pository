n = input()
x = len(n)
a = 0
for i in range(0, x):
    if n[i] == "4" or n[i] == "7":
        a = a + 1

a = str(a)
x = len(a)
p = 0
for j in range(0, x):
    if a[j] == "4" or a[j] == "7":
        p = 1
    else:
        p = 0

if p == 0:
    print("NO")
else:
    print("YES")
