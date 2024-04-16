import sys
sys_input = sys.stdin.readline
N = int(sys_input())
prices = [0] + list(map(int, sys_input().strip().split(' ')))

dp = [0] * (N + 1)
dp[1] = prices[1]

for i in range(2, N + 1):
    dp[i] = min(prices[i], min([dp[j] + dp[i - j] for j in range(1, i)]))

print(dp[N])