import sys

len_ = int(sys.stdin.readline())

for j in range(len_):
    arr = sys.stdin.readline()
    arr_brackets = [0]
    arr_end = True
    
    for i in range(len(arr)):
        if(arr[i] == '(' or arr[i] == '['):
            arr_brackets.append(arr[i])
        elif(arr[i] == ')'):
            if (arr_brackets[-1] == '('):
                arr_brackets.pop()
            else:
                arr_end = False
                break


    if(len(arr_brackets) == 1 and arr_end):
        print("YES")
    else:
        print("NO")