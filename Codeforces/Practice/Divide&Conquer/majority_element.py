n = int(input())
a = [int(x) for x in input().split()]
# freq = list(map(lambda x: a.count(x), a))
# if max(freq) > n // 2:
#     print(1)
# else:
#     print(0)

a.sort()
x = a[n // 2]
if a.count(x) > n / 2:
    print(1)
else:
    print(0)


