t = int(input())
for t in range(t):
    s = input()
    cnt_L = s.count("L")
    cnt_R = s.count("R")
    cnt_U = s.count("U")
    cnt_D = s.count("D")
    if len(s) == 1:
        y = ""
    elif min(cnt_D, cnt_U) == 0 and min(cnt_L, cnt_R) == 0:
        y = ""
    elif min(cnt_D, cnt_U) == 0:
        y = "LR"
    elif min(cnt_L, cnt_R) == 0:
        y = "UD"
    else:
        x = min(cnt_L, cnt_R)
        z = min(cnt_D, cnt_U)
        y = "L" * x + "U" * z + "R" * x + "D" * z
    print(len(y))
    print(y)

        