def solution(phone_book):    
    dic = {}
    for i in phone_book:
        dic[i] = 1
    
    for i in phone_book:
        temp = ""
        for j in i:
            temp = temp + j
            if(temp in dic and temp != i):
                return False
    
    return True