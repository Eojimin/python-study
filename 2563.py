a = int(input())
total = []
area = 0

for i in range(100):
    list_x = []
    for j in range(100):
        list_x.append(0)
    total.append(list_x)

for t in range(a):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            total[x+i][y+j] += 1

for i in range(100):
    for j in range(100):
        if total[i][j] > 0:
            area += 1
print(area)
