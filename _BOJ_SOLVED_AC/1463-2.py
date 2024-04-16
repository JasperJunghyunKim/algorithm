N = int(input())
# dp[i] = min(dp[i//3] + 1, dp[i//2] + 1, dp[i-1] + 1)

# Top Down
dp_memo = [-1] * (N + 1)
dp_memo[1] = 0

def recursive(num):
    if dp_memo[num] != -1:
        return dp_memo[num]
    
    if num % 6 == 0:
        # dp_memo[num] = min(recursive(num // 3) + 1, recursive(num // 2) + 1, recursive(num - 1) + 1)
        dp_memo[num] = min(recursive(num // 3) + 1, recursive(num // 2) + 1)
    elif num % 3 == 0:
        dp_memo[num] = min(recursive(num // 3) + 1, recursive(num - 1) + 1)
    elif num % 2 == 0:
        dp_memo[num] = min(recursive(num // 2) + 1, recursive(num - 1) + 1)
    else:
        dp_memo[num] = recursive(num - 1) + 1
    return dp_memo[num]

print(recursive(N))

# Bottom Up
dp = [0] * (N + 1)

dp[1] = 0

for i in range(2, N + 1):
    if i % 6 == 0:
        dp[i] = min(dp[i//3] + 1, dp[i//2] + 1, dp[i-1] + 1)
    elif i % 3 == 0:
        dp[i] = min(dp[i//3] + 1, dp[i-1] + 1)
    elif i % 2 == 0:
        dp[i] = min(dp[i//2] + 1, dp[i-1] + 1)
    else:
        dp[i] = dp[i-1] + 1

print(dp[N])
        