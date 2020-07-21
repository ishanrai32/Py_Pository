n = int(input())
sep_arr = []
all_arr = []
for i in range(n-2):
    q = [int(x) for x in input().split()]
    sep_arr.append(q)
    for j in range(3):
        all_arr.append(q[j])
print(all_arr)
all_arr = sorted(all_arr, key=lambda x: all_arr.count(x))
print(all_arr)
