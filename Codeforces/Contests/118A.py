s = input()

vowels = ('A', 'E', 'I', 'O', 'U', 'Y', 'a', 'e', 'i', 'o', 'u', 'y')
for i in s:
    if i in vowels:
        s = s.replace(i, "")

a = ""
for i in s:
    a = a + "." + i

a = a.lower()
print(a)