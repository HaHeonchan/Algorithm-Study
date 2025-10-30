def matrix():
    rowSum = [0] * 100
    colSum = [0] * 100
    diaSum = [0, 0]
    
    for i in range(100):
        rowInput = str(input()).strip()
        row = list(map(int, rowInput.split(" ")))
        diaSum[0] += row[i]
        diaSum[1] += row[99-i]
        rowSum[i] = sum(row)
        for j in range(len(row)):
            colSum[j] += row[j]

    return max(max(rowSum), max(colSum), max(diaSum))

def __main__():
    for i in range(10):
        testCase = int(input())
        print("#", i+1, " ", matrix(), sep="")

__main__()