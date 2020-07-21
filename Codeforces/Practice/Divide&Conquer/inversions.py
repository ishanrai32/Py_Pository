n = int(input())
a = [int(x) for x in input().split()]
inv = 0
for i in range(0, n):
    for j in range(i, n):
        if a[i] > a[j]:
            inv = inv + 1
print(inv)
