t = int(input())
for i in range(0, t):
    for j in range(0, 9):
        x = list(input())
        for k in range(0, 9):
            if x[k] == "2":
                x[k] = "1"
        y = ""
        for l in range(0, 9):
            y = y + x[l]
        print(y)
