import sys
S = int(sys.stdin.readline())
N = 1
temp_s = 0
while(True):
    temp_s += N
    N += 1
    if(temp_s > S):
        N -= 2
        break
print(N)