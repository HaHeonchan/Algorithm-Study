import sys

def mergesort(low, high):
    if(low < high):
        mid = int((low + high)/2)
        mergesort(low, mid)
        mergesort(mid+1, high)
        merge(low, mid, high)

def merge(low, mid, high):
    U = [0] * (high - low + 1)
    i = low
    j = mid + 1
    k = low

    while i <= mid and j <= high:
        if arr[i] < arr[j]:
            U[k - low] = arr[i]
            i += 1
        else:
            U[k - low] = arr[j]
            j += 1
        k += 1
    
    if i > mid:
        U[k - low:high - low + 1] = arr[j:high + 1]
    else:
        U[k - low:high - low + 1] = arr[i:mid + 1]
    
    arr[low:high + 1] = U



N = int(sys.stdin.readline())
arr = []

for i in range(N):
    OwO = int(sys.stdin.readline())
    arr.append(OwO)

mergesort(0, N-1)
for i in range(N):
    print(arr[i])