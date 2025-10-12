import sys

N = int(sys.stdin.readline())

if(N<10):
    N *= 10
    
x = 0
y = 0
z = N
ans = 0

while(z != N or ans == 0):
    x = z %10
    y = (z // 10 + x)%10
    z = x*10 + y
    ans += 1

print(ans)