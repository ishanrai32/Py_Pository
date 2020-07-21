n, k = [int(x) for x in input().split()]
scores = input().split()
max_score = int(scores[k-1])
count = 0
for i in range(0, n):
    if int(scores[i]) >= max_score and int(scores[i]) > 0:
        count = count + 1
    else:
        break

print(count)
