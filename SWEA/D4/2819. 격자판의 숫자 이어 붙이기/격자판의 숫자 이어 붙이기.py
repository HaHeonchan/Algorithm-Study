from collections import deque

dirx = [1, 0, -1, 0]
diry = [0, 1, 0, -1]

currentNum = deque()
numSet = set()

def attatchNum(arr, x, y, count):

    if(0 <= x < 4 and 0 <= y < 4):
        currentNum.append(arr[x][y])

        if count == 6:
            numtostr = ''.join(map(str, currentNum))
            numSet.add(numtostr)
        else:
            for i in range(4):
                attatchNum(arr, x + dirx[i], y+diry[i], count+1)
        currentNum.pop()




def __main__():
    global numSet
    global currentNum
    testCase = int(input())
    for i in range(testCase):
        arr = []
        numSet = set()
        currentNum = deque()
        for j in range(4):
            arrInput = list(map(int, input().split()))
            arr.append(arrInput)

        for x in range(4):
            for y in range(4):
                attatchNum(arr, x, y, 0)
        print("#", i+1, " ", len(numSet), sep='')
__main__()