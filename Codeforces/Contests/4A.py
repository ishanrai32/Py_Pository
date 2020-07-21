w = int(input())
if w>=1 and w<=100:
    r = w % 2
    q = w / 2
    if r == 0 and q != 1:
        print("YES")
    else:
        print("NO")

else:
    quit()