n, k = [int(x) for x in input().split()]
s = list(input())
c = [str(x) for x in input().split()]
c = set(c)
for i in range(n):
    x = 0
    if s[i] not in c:
        s[i] = 0
s = list(filter(lambda x: x != 0, s))


# Python3 implementation of the approach

# Function to return the count of
# valid sub-Strings
def printSubStrings(s):
    # To store distinct output subStrings
    us = set()

    # Traverse through the given String and
    # one by one generate subStrings beginning
    # from s[i].
    for i in range(len(s)):

        # One by one generate subStrings ending
        # with s[j]
        ss = ""
        for j in range(i, len(s)):
            ss = ss + s[j]
            us.add(ss)
    return len(s)


print(printSubStrings(s))
