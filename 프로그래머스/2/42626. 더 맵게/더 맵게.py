from collections import deque
import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    
    count = 0
    
    while(len(scoville)>1):
        a = heapq.heappop(scoville)
        
        if(a >= K):
            return count
        
        b = heapq.heappop(scoville)

        newFood = a + b*2
        
        heapq.heappush(scoville, newFood)
        
        count += 1
        
    if(len(scoville) == 1 and heapq.heappop(scoville) >= K):
        return count
    return -1