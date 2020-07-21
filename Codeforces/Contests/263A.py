row_no = -3
col_no = -3
row_max = "0 0 0 0 0"
for i in range(0, 5):
    row = input()
    row_no = row_no + 1
    if row > row_max:
        row_max = row
        break
row_no = abs(row_no)
n1 = row_no % 3
row_max = row_max.split()
l = len(row_max)
for i in range(0,l):
    col_no = col_no + 1
    if row_max[i] == "1":
        break
col_no = abs(col_no)
n2 = col_no % 3
n = n1 + n2

print(n)
