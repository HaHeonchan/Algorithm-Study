from collections import deque

dirX = [1, 0, -1, 0]
dirY = [0, 1, 0, -1]

def mazeRunning(maze, start):
    ssappPossible = 0
    pathNote = deque()
    pathNote.append(start)
    
    while(pathNote and ssappPossible != 1):
        x, y = pathNote.popleft()
        
        maze[x][y] = 1
        for i in range(4):
            gox = x + dirX[i]
            goy = y + dirY[i]
            if((0 <= gox < 16 and 0 <= goy < 16)
                and (maze[gox][goy] == 0)):
                pathNote.append((gox, goy))
            if(maze[gox][goy] == 3):
                ssappPossible = 1
                break
    return ssappPossible
    
def __main__():
    for _ in range(10):
        startPoint = set()
        testCase = int(input())
        mazeMap = []
        for i in range(16):
            mazeList = list(map(int, input()))
            if 2 in mazeList:
                startPoint = (mazeList.index(2), i)
            mazeMap.append(mazeList)
        print("#", testCase, " ", mazeRunning(mazeMap, startPoint), sep="")

__main__()
