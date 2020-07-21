d = int(input())  # Distance from destination
m = int(input())  # Max. distance on a full tank
n = int(input())  # No. of stations
stop = [int(x) for x in input().split()]  # Distance of stations from start point

stop.append(d)
stop.insert(0, 0)
n = n + 2
i = 0
ini = 0
x = 0
for j in range(0, n-1):
    if (stop[j+1] - stop[j] > m) or (stop[0] > m):
        x = -1
        break
while i < n:
    if x != -1:
        if stop[i] > ini + m:
            ini = stop[i-1]
            x = x + 1

        i = i + 1
    else:
        break

print(x)
