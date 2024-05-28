import sys
from collections import deque

N = int(sys.stdin.readline())
deck = deque()

for _ in range(N):
    x = list(map(int, sys.stdin.readline().split()))

    if(x[0] == 1):
        deck.appendleft(x[1])
    elif(x[0] == 2):
        deck.append(x[1])
    elif(x[0] == 3):
        if(len(deck)):
            print(deck.popleft())
        else:
            print(-1)
    elif(x[0] == 4):
        if(len(deck)):
            print(deck.pop())
        else:
            print(-1)
    elif(x[0] == 5):
        print(len(deck))
    elif(x[0] == 6):
        if(len(deck)):
            print(0)
        else:
            print(1)
    elif(x[0] == 7):
        if(len(deck)):
            print(deck[0])
        else:
            print(-1)
    elif(x[0] == 8):
        if(len(deck)):
            print(deck[-1])
        else:
            print(-1)