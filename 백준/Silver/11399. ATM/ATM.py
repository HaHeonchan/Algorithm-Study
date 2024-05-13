import sys
N = int(sys.stdin.readline().strip())
P = list(map(int, sys.stdin.readline().split()))
P.sort()

arr = [0]
result = 0
for i in range(N):
    result += P[i]+arr[i]
    arr.append(P[i]+arr[i])
print(result)