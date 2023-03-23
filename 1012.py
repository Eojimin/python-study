import sys
sys.setrecursionlimit(10000)

T = int(input())
result = []
def dfs(x, y):
    if x < 0 or x >= M or y < 0 or y >= N:
        return False
    if graph[y][x] == 1:
        graph[y][x] = 0
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

for i in range(T):
    graph = []
    count = 0
    M, N, K = map(int, input().split())
    for n in range(N):
        graph.append([0]*M)
    for pos in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1
    for m in range(M):
        for n in range(N):
            if dfs(m,n) == True:
                count += 1
    result.append(count)

for i in result:
    print(i)
