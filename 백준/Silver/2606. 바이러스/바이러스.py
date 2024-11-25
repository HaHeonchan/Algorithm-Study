import sys
        
def dfs(n, d):
    depth = d
    visited[n] = True
    for next in graph[n]:
        if(not visited[next]):
            depth = dfs(next, depth+1)
    return depth

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
    
visited = [False] * (N + 1)

print(dfs(1, 0))