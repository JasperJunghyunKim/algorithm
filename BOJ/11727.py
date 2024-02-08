########################################
# 23-12-14
n = int(input())
dp = [-1] * 1_001
dp[1] = 1
dp[2] = 3
dp[3] = 5
for i in range(4, n+1):
    dp[i] = (dp[i-1])%10007 + (2 * dp[i-2])%10007
print(dp[n]%10007)

# import sys
# input = sys.stdin.readline
# n = int(input().strip())

# # Top Down
# dp = {1:1, 2:3, 3:5}

# def num_cases(n):
#     if dp.get(n) == None:
#         dp[n] = num_cases(n-1) + 2 * num_cases(n-2)
#     return dp.get(n)

# print(num_cases(n)%10007)

# # BottomUp
# dp = [0,1,3,5,]
# for i in range(4, n+1):
#     dp.append(dp[i-1] + 2 * dp[i-2])
# print(dp[n]%10007)