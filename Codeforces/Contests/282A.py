n = int(input())
x = 0
for i in range(0, n):
    op = input()
    if op == "X++" or op == "++X":
        x = x + 1
    else:
        x = x - 1

print(x)