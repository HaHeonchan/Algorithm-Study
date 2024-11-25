import sys
        
def dfs(n):
    visited[n] = True
    for next in graph[n]:
        if(not visited[next]):
            dfs(next)

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
    
visited = [False] * (N + 1)

result = 0
for i in range(1, N + 1):
    if(visited[i] == False):
        dfs(i)
        result += 1
print(result)