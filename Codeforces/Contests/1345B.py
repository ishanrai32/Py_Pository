# Let's count the number of cards in a pyramid of height h.
# There are 2(1+2+3+⋯+h) cards standing up, and there are 0+1+2+⋯+(h−1) horizontal cards.
# So, there are 2h(h+1)/2 + (h−1)h/2 = 3/2(h^2) + 1/2(h) cards total.
t = int(input())
for t in range(0, t):
    n = int(input())
    h = 1
    py = 0
    while n >= 2:
        while h > 0:
            x = (3 / 2) * (h**2) + (1 / 2) * h
            if x > n:
                h = h + 1
            else:
                py = py + 1
            n = n - x
    print(py)