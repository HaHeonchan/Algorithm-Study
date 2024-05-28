import sys

n = int(sys.stdin.readline().strip())

for _ in range(n):
    N, M= map(int, sys.stdin.readline().split())
    Q = list(map(int, sys.stdin.readline().split()))
    
    arr = [i for i in range(0,N)]
    result = 1
    
    while True:
        nextProc = 0
        for i in range(len(Q)):
            if Q[nextProc] < Q[i]:
                nextProc = i
            
        for i in range(nextProc):
            Q.append(Q[0])
            Q.pop(0)
            arr.append(arr[0])
            arr.pop(0)
        
        if(M == arr[0]):
            print(result)
            break
        else:
            Q.pop(0)
            arr.pop(0)
            result += 1