import sys

N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline().strip()) for i in range(N)]
result = [0, 0, 0 ,0]

result[0] = round(sum(arr)/N)

arr.sort()
result[1] = arr[(N)//2]

cur_result = 0
cur_count = 0
max_count = 0
max_arr = []
for i in range(N):
    if(cur_result != arr[i]):
        cur_result = arr[i]
        cur_count = 0

    if(cur_count == max_count):
        max_arr.append(cur_result)
    
    if(cur_count > max_count):
        max_arr = []
        max_count = cur_count
        max_arr.append(cur_result)

    cur_count += 1

if(len(max_arr) > 1):
    max_arr.sort()
    result[2] = max_arr[1]
else:
    result[2] = max_arr[0]


result[3] = arr[-1] - arr[0]

 
for i in result:
    sys.stdout.write(str(i) + "\n")