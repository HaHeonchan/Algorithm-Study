import sys

N = int(sys.stdin.readline())
arr = [0]*10001
for i in range(N):
    num = int(sys.stdin.readline())
    arr[num] += 1


        
for i in range(1, 10001):
    if(arr[i] !=0):
        for j in range(arr[i]):
            sys.stdout.write(str(i) + '\n')