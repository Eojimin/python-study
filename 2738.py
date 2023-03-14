a, b = map(int, input().split())
matrix_1 = []
matrix_2 = []
matrix_sum = ""
for i in range(a):
    c = list(input().split())
    matrix_1.append(c)

for i in range(a):
    c = list(input().split())
    matrix_2.append(c)

for i in range(a):
    for j in range(b):
        d = int(matrix_1[i][j]) + int(matrix_2[i][j])
        matrix_sum += f"{d} "
    matrix_sum += "\n"

print(matrix_sum)