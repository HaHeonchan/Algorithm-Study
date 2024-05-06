import sys

N = int(sys.stdin.readline())

count = 0

while(N >= 3):
    if(N%5 == 0):
        N -= 5
        count +=1
    else:
        N -= 3
        count +=1


if(N>0):
    print(-1)
else:
    print(count)