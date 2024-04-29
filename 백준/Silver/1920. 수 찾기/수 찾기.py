import sys

n = int(sys.stdin.readline())
n_arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_arr = list(map(int, sys.stdin.readline().split()))

n_arr.sort()
for i in range(m):
    ans = 0
    high = n - 1
    low = 0
    mid = int((low+high)/2)
    
    while(high >= low):
        mid = int((low+high)/2)

        if(mid < 0):
            break
        
        if(n_arr[mid] == m_arr[i]):
            ans = 1
            break
        elif(n_arr[mid]>m_arr[i]):
            high = mid - 1
        else:
            low = mid +1
    print(ans)