from collections import deque

matchParentheses = {
    '{': '}',
    '[': ']',
    '(': ')',
    '<': '>'
}
parentheses = ['(', '[', '{', '<']

def owo(text):
    result = 1
    que = deque()
    que.append(text[0])
    for i in range(1, len(text)-1):

        if(text[i] in parentheses):
            que.append(text[i])
        elif (matchParentheses[que[-1]] == text[i]):
            que.pop()
        else:
            result = 0
            break
    if not que:
        result = 0
    return result

def __main__():
    for i in range(10):
        arrLength = int(input())
        text = list(map(str, input()))
        print("#", i+1, " ", owo(text), sep='')
__main__()