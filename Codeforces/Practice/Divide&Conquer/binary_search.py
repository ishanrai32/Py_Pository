def bsearch(lst, x):
    start = 0
    end = len(lst) - 1
    while start <= end:
        mid = (start + end) // 2

        if x > lst[mid]:
            start = mid + 1
        elif x < lst[mid]:
            end = mid - 1
        else:
            return mid
    return -1

a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
n = a.pop(0)
k = b.pop(0)
indices = []
for i in range(0, k):
    x = bsearch(a, b[i])
    indices.append(x)
print(*indices)
