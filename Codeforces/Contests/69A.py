n = int(input())
Fx = Fy = Fz = 0
for i in range(0, n):
    x, y, z = [int(x) for x in input().split()]
    Fx = Fx + x
    Fy = Fy + y
    Fz = Fz + z
if Fx == 0 and Fy == 0 and Fz == 0:
    print("YES")
else:
    print("NO")