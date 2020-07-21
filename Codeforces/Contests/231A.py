n = int(input())
count = 0
for i in range(0, n):
    a, b, c = [int(x) for x in input().split()]
    yes = a + b + c
    if yes >= 2:
        count = count + 1

print(count)
