t = int(input())
for i in range(0, t):
    n = int(input())
    if n == 1 or n == 2:
        x = 0
    elif n % 2 == 0:
        x = n // 2
        x = x - 1
    else:
        x = n // 2
    print(x)
