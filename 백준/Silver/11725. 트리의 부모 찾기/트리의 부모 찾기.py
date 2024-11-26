import sys
from collections import deque

def bfs(n):
    stack = deque([])
    stack.append(n)
    bfs_result.append(n)
    while stack:
        current = stack.popleft()
        for next in graph[current]:
            if(visited[next] == 0):
                visited[next] = current
                bfs_result.append(next)
                stack.append(next)
        
def print_arr(arr):
    for i in arr:
        print(i)
  
N = int(sys.stdin.readline())
graph = [[] for _ in range(N + 1)]
for _ in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    graph[i].sort()

bfs_result = []
visited = [0] * (N + 1)
bfs(1)
print_arr(visited[2:])