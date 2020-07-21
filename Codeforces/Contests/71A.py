n = int(input())
for i in range(0, n):
    abb = str(input())
    l = len(abb)
    if l > 10 :
        print(abb[0], l - 2, abb[-1], sep='')
    else:
        print(abb)
