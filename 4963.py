def dfs(x, y):
    if x >= w or x < 0 or y >= h or y < 0:
        return False

    if graph[y][x] == 1:
        graph[y][x] = 0
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        dfs(x+1, y+1)
        dfs(x+1, y-1)
        dfs(x-1, y+1)
        dfs(x-1, y-1)
        return True
    else:
        return False

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = []
    result = 0
    for i in range(h):
        land = list(map(int, input().split()))
        graph.append(land)

    for i in range(w):
        for j in range(h):
            if dfs(i, j):
                result += 1

    print(result)
