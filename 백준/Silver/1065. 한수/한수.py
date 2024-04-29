import sys

N = int(sys.stdin.readline())

def hansu(num):
    if num <= 99:
        return True
    
    arr = [int(d) for d in str(num)]
    diff = arr[1] - arr[0]
    
    for i in range(1, len(arr), 1):
        if arr[i] - arr[i-1] != diff:
            return False
    return True


count = 0
for i in range(1, N+1):
    if hansu(i):
        count += 1

print(count)