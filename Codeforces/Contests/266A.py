n = int(input())
stones = input()
rem = 0
for i in range(0, n - 1):
    if stones[i] == stones[i+1]:
        rem = rem + 1
print(rem)