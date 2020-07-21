import numpy as np
n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
a.sort(reverse=True)
b.sort(reverse=True)
c = np.multiply(a, b)
print(sum(c))
