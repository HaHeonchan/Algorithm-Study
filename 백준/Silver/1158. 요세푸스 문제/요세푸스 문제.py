import sys

N, K = map(int, sys.stdin.readline().split())
arr = []
result = []

for i in range(1, N+1):
    arr.append(i)

p_K = 0
for i in range(1, N+1):
    p_K += K-1
    p_K %= len(arr)
    result.append(arr.pop(p_K))

print('<', end = '')
for i in result:
    print(i, end = '')
    if(result[-1]==i):
        print('>')
        break
    else:
        print(', ', end = '')