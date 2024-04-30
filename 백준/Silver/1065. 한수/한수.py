import sys

N = int(sys.stdin.readline())

def hansu(num):
    if num <= 99:
        return True
    
    arr = [int(d) for d in str(num)]
    diff = arr[1] - arr[0]
    
    for i in range(1, len(arr), 1):
        if arr[i] - arr[i-1] != diff:
            return False
    return True


count = 0
for i in range(1, N+1):
    if hansu(i):
        count += 1

print(count)

#이 문제를 이해하고 푸는 과정에서 입력값을 쪼개는것이 전체 풀이 시간에 절반을 썼었던것 같다
#결국 구글링을 통해 이런 엄청난 방법을 통해 한줄만에 구하는 방법을 알아냈으며
#내가 힘들게 짠 코드는 가차없이 지워졌다
#다음에는 어렵다 싶으면 다른 방법이 있는지도 찾아보아야 할 것 같다
