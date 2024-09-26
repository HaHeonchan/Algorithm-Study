import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
result = 0

i = 0
j = 0
while(j <= len(arr)):
    if(sum(arr[i:j]) > M):
        i += 1
    elif(sum(arr[i:j]) < M):
        j += 1
    else:
        result += 1
        i += 1
        
print(result)