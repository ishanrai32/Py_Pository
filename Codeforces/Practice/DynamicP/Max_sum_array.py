# Find the sub-array that gives the maximum sum in an array of numbers
# Array input by space separated integers
a = [int(x) for x in input().split()]
n = len(a)
sum_sub_array = 0
max_sum = 0
for i in range(0, n):
    sum_sub_array = max(a[i], sum_sub_array + a[i])
    # Check which value is more and take it, if the element is negative the sub array till only the previous element
    max_sum = max(max_sum, sum_sub_array)
print(max_sum)

