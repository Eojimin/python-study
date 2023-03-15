a = int(input())
row = 1
column = 1
column_count = 1
row_count = 2
odd = 1
while True:
    if a >= column and a <= row:
        break
    column += column_count
    column_count += 1
    row += row_count
    row_count += 1
    odd += 1

top = 1
bottom = column_count
a -= column

while a > 0:
    top += 1
    bottom -= 1
    a -= 1
if column_count % 2 == 0:
    print(f"{top}/{bottom}")
else:
    print(f"{bottom}/{top}")