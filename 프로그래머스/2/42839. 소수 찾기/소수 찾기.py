import itertools

def solution(numbers):
    answer = 0
    numarr = [x for x in numbers]
    sosulist = []
    for _ in range(1, len(numarr)+1):
        perNum = list(itertools.permutations(numbers, _))
        perNumArr = [int("".join(x)) for x in perNum]
        perNumSet = set(perNumArr)
        for i in perNumSet: 
            
            sosu = True
            for j in range(2, i // 2 +1):
                if(i % j == 0):
                    sosu = False
                    break
            if(sosu and i > 1 and i not in sosulist):
                answer += 1
                sosulist.append(i)
    return answer