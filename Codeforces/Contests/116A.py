n = int(input())
no = 0
max_no = 0
for i in range(0, n):
    a, b = [int(x) for x in input().split()]
    no = no - a + b
    if no > max_no:
        max_no = no
print(max_no)
