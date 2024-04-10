import sys

while(True):
    arr = sys.stdin.readline()
    arr_brackets = [0]
    arr_end = True

    if(arr[0] == '.'):
          break
    
    for i in range(len(arr)):
        if(arr[i] == '.'):
            break
        elif(arr[i] == '(' or arr[i] == '['):
            arr_brackets.append(arr[i])
        elif(arr[i] == ')'):
            if (arr_brackets[-1] == '('):
                arr_brackets.pop()
            else:
                arr_end = False
                break
        elif(arr[i] == ']'):
            if (arr_brackets[-1] == '['):
                arr_brackets.pop()
            else:
                arr_end = False
                break

    if(len(arr_brackets) == 1 and arr_end == True):
        print("yes")
    else:
        print("no")