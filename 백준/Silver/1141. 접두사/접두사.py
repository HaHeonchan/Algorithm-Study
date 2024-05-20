import sys

N = int(sys.stdin.readline())
inputs = [input() for _ in range(N)]

inputs = sorted(inputs, key=len)
inputs.reverse()

arr = []

for i in range(N):
    result = True
    for j in range(len(arr)):
        if(arr[j].find(inputs[i]) == 0 or inputs[i].find(arr[j]) == 0):
            result = False
            break
    if(result):
        arr.append(inputs[i])
print(len(arr))