from collections import deque

def que():
    inputarr = input(str())
    arr = list(map(int, inputarr.strip().split(" ")))
    
    point = 0
    minus = 1
    arrq = deque(arr)

    while(arrq[-1] != 0):
        arrq.append(max(arrq.popleft()-minus, 0))

        if(minus >= 5):
            minus = 1
        else:
            minus += 1

    for i in range(7):
        print(arrq.popleft(), end=" ")
    print(arrq.popleft())
    
    
def __main__():
    for _ in range(10):
        tcase = str(input())
        print("#", _+1, sep="", end=" ")
        que()
__main__()
