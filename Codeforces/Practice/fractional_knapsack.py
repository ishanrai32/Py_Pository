def fractional_knapsack(value, weight, capacity):
    """Return maximum value of items and their fractional amounts.

    (max_value, fractions) is returned where max_value is the maximum value of
    items with total weight not more than capacity.
    fractions is a list where fractions[i] is the fraction that should be taken
    of item i, where 0 <= i < total number of items.

    value[i] is the value of item i and weight[i] is the weight of item i
    for 0 <= i < n where n is the number of items.

    capacity is the maximum weight.
    """
    # index = [0, 1, 2, ..., n - 1] for n items
    index = list(range(len(value)))
    # contains ratios of values to weight
    ratio = [v / w for v, w in zip(value, weight)]
    # index is sorted according to value-to-weight ratio in decreasing order
    # This is the line that is the most powerful in all of the code, sorting wrt to V/W ratio
    index.sort(key=lambda i: ratio[i], reverse=True)

    max_value = 0
    fractions = [0] * len(value)
    for i in index:
        if weight[i] <= capacity:
            # If wt of object <= Capacity we include all of it in the knapsack
            fractions[i] = 1
            # The value increases by the value of the object
            max_value = max_value + value[i]
            # The capacity of the knapsack decreases
            capacity = capacity - weight[i]
        else:
            # If wt of object > Capacity then we can only take a part of it
            fractions[i] = capacity / weight[i]
            max_value = max_value + value[i] * capacity / weight[i]
            break

    return max_value, fractions


n, C = [int(x) for x in input().split()]
V = []
W = []
for i in range(0, n):
    x, y = [float(x) for x in input().split()]
    V.append(x)
    W.append(y)

max_value, fractions = fractional_knapsack(V, W, C)
print(round(max_value, 4))
