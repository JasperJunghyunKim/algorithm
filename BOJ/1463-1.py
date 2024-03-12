#
# 24-03-12
# Bottom Up, Top Down
#

import sys
sys_input = sys.stdin.readline
n = int(sys_input().strip())

# Bottom Up
memo = [0 for _ in range(1_000_001)]
memo[1] = 0
memo[2] = 1
memo[3] = 1
memo[4] = 2

for i in range(5, n + 1):
    if i % 2 and i % 3:
        memo[i] = memo[i-1] + 1
    elif i % 2 and not i % 3:
        memo[i] = min(memo[i-1], memo[i//3]) + 1
    elif not i % 2 and i % 3:
        memo[i] = min(memo[i-1], memo[i//2]) + 1
    else:
        memo[i] = min(memo[i-1], memo[i//2], memo[i//3]) + 1

print(memo[n])

# Top Down
# Recursive Error 가 발생했는데, 
# 2, 3 으로 모두 나눠 떨어지는 경우에 make_one(n-1) 을 제거하여 해결
dp = {1:0, 2:1, 3:1}
def make_one(n):
    
    if n in dp: return dp[n]


    if n % 2 and n % 3:
        dp[n] = make_one(n-1) + 1
    elif n % 2 and not n % 3:
        dp[n] = min(make_one(n-1), make_one(n//3)) + 1
    elif not n % 2 and n % 3:
        dp[n] = min(make_one(n-1), make_one(n//2)) + 1
    else:
        dp[n] = min(make_one(n//2), make_one(n//3)) + 1
        # dp[n] = min(make_one(n-1), make_one(n//2), make_one(n//3)) + 1
    return dp[n]

print(make_one(n))