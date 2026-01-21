def solution(numbers):
    numberString = [str(x) for x in numbers]
    
    numberString.sort(key= lambda x : x*4, reverse=True)

    answer = ""
    for i in numberString:
        answer += str(i)
        
    if answer[0] == '0':
        return "0"
    return answer