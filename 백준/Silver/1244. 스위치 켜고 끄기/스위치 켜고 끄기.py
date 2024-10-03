import sys

switch_num = int(sys.stdin.readline())
switch_arr = list(map(int, sys.stdin.readline().split()))

student_num = int(sys.stdin.readline())

for i in range(student_num):
    student, location = map(int, input().split())

    if student == 1:
        temp_loc = location
        while location <= switch_num:
            switch_arr[location - 1] = 1 - switch_arr[location - 1]
            location += temp_loc
            
    elif student == 2:
        switch_arr[location - 1] = 1 - switch_arr[location - 1]
        
        low = location - 2
        high = location
        while low >= 0 and high < switch_num and switch_arr[low] == switch_arr[high]:
            switch_arr[low] = 1 - switch_arr[low]
            switch_arr[high] = 1 - switch_arr[high]
            low -= 1
            high += 1

for i in range(switch_num):
    print(switch_arr[i], end=' ')
    if (i + 1) % 20 == 0:
        print()