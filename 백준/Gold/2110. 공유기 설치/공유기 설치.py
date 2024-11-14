import sys

def sulchi_ssap_possible(arr, g, l):
    setting = 1
    current = 0
    for i in range(len(arr)):
        if(arr[i] - arr[current] >= l):
            setting += 1
            current = i
    if(setting >= g):
        return 'high'
    else:
        return 'low'
    
def sulchi_gisa(home, gong_u_gi):
    home.sort()
    low = 1
    high = home[-1] - home[0]

    result = 0
    
    while(high >= low):
        mid = (low + high) // 2
        
        ans = sulchi_ssap_possible(home, gong_u_gi , mid)
        
        if (ans == 'high'):
            low = mid + 1
            result = mid
        else:
            high = mid - 1

    return result



N, C = map(int, sys.stdin.readline().split())


A = [int(sys.stdin.readline().strip()) for _ in range(N)]

result = sulchi_gisa(A, C)
# result = NGE(A)

print(result)