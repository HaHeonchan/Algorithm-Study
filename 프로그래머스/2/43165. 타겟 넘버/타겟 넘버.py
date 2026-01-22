def findTarget(numbers, dir, result, target, pointer):
    if(len(numbers) == pointer):
        if(target == result):
            return 1
        else:
            return 0
    num = numbers[pointer]
    a = findTarget(numbers, 1, result + num*dir, target, pointer+1)
    b = findTarget(numbers, -1, result + num*dir, target, pointer+1)
    return a + b

def solution(numbers, target):
    answer = findTarget(numbers, 1, 0, target, 0)
    answer += findTarget(numbers, -1, 0, target, 0)
    return answer/2