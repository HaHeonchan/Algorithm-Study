import sys

def dp(n):
    if n == 1:
        return 3
    elif n == 2:
        return 7
    else:
        dp = [0 for _ in range(n + 1)]
        dp[1] = 3
        dp[2] = 7
        for i in range(3, n+1):
            dp[i] = (2*dp[i-1] + dp[i-2]) % 9901
        return dp[n]
        
def main():
    n = int(sys.stdin.readline())
    print(dp(n))
main()