import sys

N = int(sys.stdin.readline())
arr = [list(map(str, sys.stdin.readline().split())) for _ in range(N)]

grading = [False] * N

grade = ["A+", "A", "B+", "B", "C+", "C", "D+", "D", "F"]
grade_num = [97, 90, 87, 80, 77, 70, 67, 60, 0]

for i in range(9):
    gn = grade_num[i]
    g = grade[i]
    for j in range(N):
        if(not grading[j] and int(arr[j][1]) >= gn):
            arr[j][1] = g
            grading[j] = True

for i in arr:
    print(i[0], end=' ')
    print(i[1])