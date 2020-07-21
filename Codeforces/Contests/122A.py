n = int(input())
lucky = 0
almost_lucky = 0
for i in range(1, n + 1):
    i_str = str(i)
    lst = list(i_str)
    l = len(lst)
    for j in range(0, l):
        if (lst[j] == "4") or (lst[j] == "7"):
            lucky = 1
        else:
            lucky = 0
            break
    if lucky == 1:
        r = n % i
        if r == 0:
            almost_lucky = 1

if almost_lucky == 1:
    print("YES")
else:
    print("NO")
