players = list(input())
l = len(players)
count = 1
for i in range(0, l - 1):
    if players[i] == players[i + 1]:
        count = count + 1
    else:
        count = 1

    if count == 7:
        break

if count == 7:
    print("YES")
else:
    print("NO")
