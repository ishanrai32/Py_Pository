n = int(input())
s = [int(x) for x in input().split()]
s.sort()
x = len(s)
a = s[x-1]
b = s[x-2]
max_prod = a * b
print(max_prod)

