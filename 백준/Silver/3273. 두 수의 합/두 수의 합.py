import sys

n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline().strip())
result = 0

arr = a[:n]
arr.sort()

'''
for i in range(len(arr)):
    low = i
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2

        if i == mid:
            break
        
        if dup == arr[i]:
            break
        
        if arr[mid] > x - arr[i]:
            high = mid - 1
        elif arr[mid] < x - arr[i]:
            low = mid + 1
        else:
            result += 1
            if(arr[mid] == arr[i]):
                dup = arr[i]
            break
'''

low = 0
high = len(arr)-1
while(low < high):
    if(arr[high] + arr[low] > x):
        high -= 1
    elif(arr[high] + arr[low] < x):
        low += 1
    else:
        result += 1
        high -= 1
        low += 1
        
print(result)