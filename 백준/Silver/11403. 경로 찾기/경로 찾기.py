import sys

def ser(i, j):
    if(arr[i][j] == 1):
        for x in range(N):
            if(arr[j][x] == 1):
                arr[i][x] = 1
    if(arr[j][i] == 1):
        for x in range(N):
            if(arr[i][x] == 1):
                arr[j][x] = 1
                
N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        ser(i, j)
        
for i in range(N):
    for j in range(N):
        print(arr[i][j], end=' ')
    print('')