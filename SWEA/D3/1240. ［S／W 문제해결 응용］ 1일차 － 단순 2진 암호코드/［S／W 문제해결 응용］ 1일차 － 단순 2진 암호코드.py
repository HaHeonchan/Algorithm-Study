CODE = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}

def mat():
    resultsArr = []
    complite = 0
    n, m = map(int, input().split(" "))
    for i in range(n):
        rowInput = list(map(str, input()))
        if("1" in rowInput and complite == 0):
            endIndex = m
            for j in range(m-1, -1, -1):
                if(rowInput[j] == '1'):
                    endIndex = j + 1
                    break
            for j in range(8):
                currentEndIndex = endIndex-(7)*(j)
                arr7 = rowInput[currentEndIndex-7:currentEndIndex]
                str7 = "".join(arr7)
                resultsArr.append(CODE[str7])
            complite = 1
    resultsArr.reverse()
    oddSum = resultsArr[0] + resultsArr[2] + resultsArr[4] + resultsArr[6]
    evenSum = resultsArr[1] + resultsArr[3] + resultsArr[5] + resultsArr[7]
    totalSum = oddSum * 3 + evenSum
    if(totalSum % 10 == 0):
        return sum(resultsArr)
    else:
        return 0
                
                

def __main__():
    testCases = int(input())
    for _ in range(testCases):
        print("#", _+1, " ", mat(), sep="")


__main__()