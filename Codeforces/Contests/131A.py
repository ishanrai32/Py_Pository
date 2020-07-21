s = input()
l = len(s)
s1 = s[0]
s2 = s[1:]
if s.isupper():
    x = 1
elif s1.islower() and s2.isupper():
    x = 1
elif s1.islower() and len(s2) == 0:
    x = 1
else:
    x = 0

if x == 1:
    s = s.swapcase()
    print(s)
else:
    print(s)




