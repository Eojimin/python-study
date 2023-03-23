from collections import deque
N, M, V = map(int, input().split())

graph = [[]]

for i in range(N):
    graph.append([])

for i in range(1, M+1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    graph[x].sort()
    graph[y].sort()

visited_bfs = [False] * (N+1)
visited_dfs = [False] * (N+1)

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


dfs(graph, V, visited_dfs)
print("")
bfs(graph, V, visited_bfs)
