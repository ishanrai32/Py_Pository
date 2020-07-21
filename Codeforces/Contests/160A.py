n = int(input())
a = input().split()
a = [int(i) for i in a]
s = 0
s1 = 0
count = 0
for j in range(0, n):
    s = s + int(a[j])
s = s // 2

a.sort(reverse=True)
for k in range(0, n):
    if s1 > s:
        break
    else:
        s1 = s1 + int(a[k])
        count = count + 1
print(count)