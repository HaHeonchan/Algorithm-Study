import sys
stack = []
com = int(sys.stdin.readline())

for i in range(com):
    inputs = sys.stdin.readline().split()
    
    if inputs[0] == "push":
        stack.append(inputs[1])
        
    elif inputs[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
            
    elif inputs[0] == "size":
        print(len(stack))
        
    elif inputs[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
            
    elif inputs[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
"""
문제를 푸는 과정에서 에러를 해결하기 위해 알아보다가
풀이에 도움이 될만한 것을 배우게 되었다.
sys.stdin.readline()를 이용해 입력을 받으면 input보다 더 빠르고
배열에 접근할때 배열의 끝 주소가 아닌 -1로 쉽게 접근 할 수 있었다
안타깝게도 오류 원인은 단순 오타였다
"""
