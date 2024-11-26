import sys
from collections import deque

def dfs(n):
    visited[n] = True
    dfs_result.append(n)
    for next in graph[n]:
        if(not visited[next]):
            dfs(next)

def bfs(n):
    stack = deque([])
    stack.append(n)
    bfs_result.append(n)
    visited[n] = True
    while stack:
        current = stack.popleft()
        for next in graph[current]:
            if(not visited[next]):
                visited[next] = True
                bfs_result.append(next)
                stack.append(next)
        
def print_arr(arr):
    for i in arr:
        print(i, end=' ')
    print('')
  
N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    graph[i].sort()

dfs_result = []
visited = [False] * (N + 1)
dfs(V)
print_arr(dfs_result)

bfs_result = []
visited = [False] * (N + 1)
bfs(V)
print_arr(bfs_result)