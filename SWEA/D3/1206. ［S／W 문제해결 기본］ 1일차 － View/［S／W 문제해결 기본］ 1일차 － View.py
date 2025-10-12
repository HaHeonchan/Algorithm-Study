from collections import deque

arr = []
for i in range(10):
    N = int(input())
    A = list(map(int, input().split()))
    endPoint = 4
    queue = deque(A[0:5])
    score = 0
    
    while(len(A)-1 >= endPoint):
        maxNum = -1
        for i in range(5):
            if(maxNum <= queue[i] and i != 2):
                maxNum = queue[i]
        score += max(queue[2] - maxNum, 0)
        
        if(endPoint != N-1):
            queue.popleft()
            endPoint += 1
            queue.append(A[endPoint])
        else:
            break
        
    arr.append(score)

for i in range(0, len(arr)):
    print("#", i+1, " ", arr[i], sep="")