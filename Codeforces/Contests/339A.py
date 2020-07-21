s = input().split("+")
s.sort()
l = len(s)
a = ""
for i in range(0, l):
    a = a + s[i]
    if i == l - 1:
        break
    a = a + "+"
print(a)
