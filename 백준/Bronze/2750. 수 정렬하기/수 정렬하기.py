import sys

def mergeSort(l, h):
    if(l < h):
        m = int((h + l)/2)
        mergeSort(l, m)
        mergeSort(m + 1, h)
        merge(l, m, h)

def merge(l, m, h):
    m_arr = [0] * (h - l + 1)
    i = l
    k = l
    j = m + 1

    while(i <= m and j <= h):
        if(arr[i] > arr[j]):
            m_arr[k-l] = arr[i]
            i += 1
        else:
            m_arr[k-l] = arr[j]
            j += 1
        k += 1
    
    if(i > m):
        m_arr[k - l : h - l + 1] = arr[j : h + 1]
    else:
        m_arr[k-l : h - l + 1] = arr[i : m + 1]

    arr[l:h + 1] = m_arr
        

N = int(sys.stdin.readline())
arr = []

for i in range(N):
    n = int(sys.stdin.readline())
    arr.append(n)

mergeSort(0, len(arr)-1)

for i in range(len(arr)-1, -1, -1):
    print(arr[i])