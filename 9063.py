N = int(input())
list_x = []
list_y = []

for n in range(N):
    x, y = map(int, input().split())
    list_x.append(x)
    list_y.append(y)

width = max(list_x) - min(list_x)
height = max(list_y) - min(list_y)

if N > 1:
    print(width*height)
else:
    print(0)
