import sys
sys.setrecursionlimit(10**6)

def Z(x, y, s):
    global result
    global i
    
    if s == 1:
        if x == r and y == c:
            print(i+0)
        elif x == r and y+1 == c:
            print(i+1)
        elif x+1 == r and y == c:
            print(i+2)
        elif x+1 == r and y+1 == c:
            print(i+3)
        result = 1
    
    if result == -1:
        s = s // 2
        if r < x + s and c < y + s:
            Z(x, y, s)
        elif r < x + s and c >= y + s:
            i += s * s
            Z(x, y + s, s)
        elif r >= x + s and c < y + s:
            i += s * s * 2
            Z(x + s, y, s)
        elif r >= x + s and c >= y + s:
            i += s * s * 3
            Z(x + s, y + s, s)

N, r, c = map(int, sys.stdin.readline().split())
size = 2**N
result = -1
i = 0
Z(0, 0, size)
    
