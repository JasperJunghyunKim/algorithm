import sys
sys_input = sys.stdin.readline

N = int(sys_input().strip())
wine = [0 for _ in range(N + 1)]
for i in range(1, N + 1):
    wine[i] = int(sys_input().strip())

dp = [0] * (N + 1)
dp[0] = 0
if N == 1:
    print(wine[1])
    exit()
elif N == 2:
    print(wine[1] + wine[2])
    exit()
dp[1] = wine[1]
dp[2] = wine[1] + wine[2]
dp[3] = max(wine[2] + wine[3], wine[3] + wine[1], wine[1] + wine[2])
for i in range(4, N + 1):
    dp[i] = max(wine[i] + wine[i-1] + dp[i-3], wine[i] + dp[i-2], dp[i-1])
print(dp[N])