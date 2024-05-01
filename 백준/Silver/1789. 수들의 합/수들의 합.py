import sys
S = int(sys.stdin.readline())
N = 1
temp_s = 0
while(True):
    temp_s += N
    if(temp_s > S):
        N -= 1
        break
    N += 1
print(N)