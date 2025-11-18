from collections import deque

def suplyLoad(size, suplyMap):

    dirx = [1, 0, -1, 0]
    diry = [0, 1, 0, -1]

    gotoList = deque()
    gotoList.append((0, 0))

    visitList = [[-1]*size for _ in range(size)]
    visitList[0][0] = 0

    while gotoList:
        x, y = gotoList.popleft()

        minTime = 0
        nextDirList = []

        for i in range(4):
            gotoX = x + dirx[i]
            gotoY = y + diry[i]
            if 0 <= gotoX < size and 0 <= gotoY < size:
                if (visitList[gotoX][gotoY] == -1
                        or visitList[gotoX][gotoY] > visitList[x][y] + suplyMap[gotoX][gotoY]):
                    visitList[gotoX][gotoY] = visitList[x][y] + suplyMap[gotoX][gotoY]

                    gotoList.append((gotoX, gotoY))

    return visitList[size-1][size-1]

testCase = int(input())
for i in range(testCase):
    suplyMap = []
    size = int(input())

    for _ in range(size):
        mapLine = list(map(int, input()))
        suplyMap.append(mapLine)

    print("#", i+1, " ", suplyLoad(size, suplyMap), sep="")