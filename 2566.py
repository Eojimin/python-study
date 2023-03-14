total = []
max_result = 0
row = 0
column = 0
for i in range(9):
    a = list(map(int, input().split()))
    total.append(a)

for i in range(9):
    for j in range(9):
        if total[i][j] >= max_result:
            max_result = total[i][j]
            row = i + 1
            column = j + 1

print(max_result)
print(f"{row} {column}")