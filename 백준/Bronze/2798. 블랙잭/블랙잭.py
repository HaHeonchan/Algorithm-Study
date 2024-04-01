import sys

N, M = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))

max_sum = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            c_sum = card[i] + card[j] + card[k]
            if c_sum <= M and c_sum > max_sum:
                max_sum = c_sum

print(max_sum)