import sys
import math

n = int(sys.stdin.readline().strip())

while True:
    ans = True

    if n == 1:
        ans = False
        
    if(ans):
        for i in range (2, int(math.sqrt(n) + 1)):
            if n % i == 0:
                ans = False
                break

    if(ans):
        arr = list(str(n))
        for i in range(0, len(arr) // 2):
            if arr[i] != arr[len(arr) - i - 1]:
                ans = False
                break
        
    if (ans):
        print(n)
        break
    else:
        n += 1