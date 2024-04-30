import sys
queue = []
com = int(sys.stdin.readline())

for i in range(com):
    inputs = sys.stdin.readline().split()
    
    if inputs[0] == "push":
        queue.append(inputs[1])
        
    elif inputs[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
            
    elif inputs[0] == "size":
        print(len(queue))
        
    elif inputs[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
            
    elif inputs[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            
    elif inputs[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])