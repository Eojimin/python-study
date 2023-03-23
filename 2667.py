N = int(input())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

grop = 1
def dfs(x, y):
        if x <= -1 or x >= N or y <= -1 or y >= N:
            return False
        if graph[x][y] == 1:
            graph[x][y] = str(grop)
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y+1)
            dfs(x, y-1)
            return True

for i in range(N):
    for j in range(N):
        if dfs(i, j) == True:
            grop += 1
print(grop-1)
count_list = []
for i in range(1, grop):
    count = 0
    for j in range(N):
        count += graph[j].count(str(i))
    count_list.append(count)
count_list.sort()
for i in count_list:
    print(i)


