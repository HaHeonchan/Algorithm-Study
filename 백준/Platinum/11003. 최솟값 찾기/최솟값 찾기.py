from collections import deque
import sys

N, L = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

result = [] #결과
min_queue = deque() #큐

for i in range(N):

    #큐의 맨 뒤에 값이 지금 값보다 크면 나가리
    while len(min_queue) != 0 and A[min_queue[-1]] > A[i]:
        min_queue.pop()
    
    #큐에 현재 값 추가
    min_queue.append(i)

    # L의 범위 밖의 인덱스도 나가리
    if min_queue[0] <= i - L:
        min_queue.popleft()

    # 큐의 맨 앞의 값을 추가(범위중 가장 작은 값)
    result.append(A[min_queue[0]])

for i in result:
    print(i, end=' ')