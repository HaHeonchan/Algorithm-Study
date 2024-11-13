import sys

def NGE(arr):
    result = [-1] * len(arr)
    stack = []

    for i in range(len(arr)):
        while(len(stack) != 0 and arr[stack[-1]] < arr[i]):
            index = stack.pop()
            result[index] = arr[i]
        stack.append(i)

    return result

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

result = NGE(A)

for i in result:
    print(i, end = ' ')