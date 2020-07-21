def countdistinct(s):
    m = {}
    m = m.fromkeys(s, 0)
    for i in range(len(s)):
        # increase the frequency
        # of character
        m[s[i]] += 1

    return len(m.keys())


def mostfrequent(arr, n):
    # Sort the array
    arr.sort()

    # find the max frequency using
    # linear traversal
    max_count = 1
    res = arr[0]
    curr_count = 1

    for i in range(1, n):
        if arr[i] == arr[i - 1]:
            curr_count += 1

        else:
            if curr_count > max_count:
                max_count = curr_count
                res = arr[i - 1]

            curr_count = 1

    # If last element is most frequent
    if curr_count > max_count:
        max_count = curr_count
        res = arr[n - 1]

    return max_count


t = int(input())
for i in range(0, t):
    n = int(input())
    a = [int(x) for x in input().split()]
    z = countdistinct(a)
    y = mostfrequent(a, n)

    # Remove the most frequent one from distinct characters
    z = z - 1

    if y > z:
        if y-1 < z+1:
            print(y-1)
        else:
            print(z+1)
    elif z >= y:
        print(y)





