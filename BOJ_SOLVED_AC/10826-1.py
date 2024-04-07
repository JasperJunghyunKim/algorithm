import sys
sys.setrecursionlimit(10_001)

N = int(input().strip())
if N == 0:
    print(0)
    exit()
elif N == 1:
    print(1)
    exit()
dp = [0 for _ in range(N + 1)]
dp[1] = 1
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    if not dp[n-1]:
        dp[n-1] = fibo(n-1)
    if not dp[n-2]:
        dp[n-2] = fibo(n-2)
    return dp[n-1] + dp[n-2]

print(fibo(N))
