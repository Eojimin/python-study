N = int(input())
graph = []

result = 0
result_2 = 0
for i in range(N):
    line = list(input())
    graph.append(line)


def dfs(x, y, color):
    if x >= N or y >= N or x < 0 or y < 0:
        return False

    if graph[x][y] == color:
        if color == "R" or color == "G":
            graph[x][y] = "R1"
        else:
            graph[x][y] = 0
        dfs(x+1, y, color)
        dfs(x-1, y, color)
        dfs(x, y+1, color)
        dfs(x, y-1, color)
        return True
    else:
        return False

for i in range(N):
    for j in range(N):
        if dfs(i, j, 'B'):
            result += 1
            result_2 += 1
        if dfs(i, j, 'R') or dfs(i, j, 'G'):
            result += 1

for i in range(N):
    for j in range(N):
        if dfs(i, j, 'R1'):
            result_2 += 1

print(result, result_2)
