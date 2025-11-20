
def ladder():
    startPoints = {}

    startInput = list(map(int, input().split()))
    for i in range(100):
        if(startInput[i] == 1):
            startPoints[i] = i
            
    for i in range(98):
        stateInput = list(map(int, input().split()))
        
        for j in startPoints:
            if(startPoints[j] != 0 and stateInput[startPoints[j]-1] == 1):
                while(startPoints[j] != 0 and stateInput[startPoints[j]-1] == 1):
                    startPoints[j] -= 1
            elif(startPoints[j] != 99 and stateInput[startPoints[j]+1] == 1):
                while(startPoints[j] != 99 and stateInput[startPoints[j]+1] == 1):
                    startPoints[j] += 1
            else:
                pass
            
    endInput = list(map(int, input().split()))
    Xpoint = endInput.index(2)
    result = -1
    for i in startPoints:
        if(startPoints[i] == Xpoint):
            result = i
            break
    return result

def __main__():
    for _ in range(10):
        testCase = int(input())

        print("#", testCase, " ", ladder(), sep="")
__main__()
