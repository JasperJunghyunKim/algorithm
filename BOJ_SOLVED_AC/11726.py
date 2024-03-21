import sys
input = sys.stdin.readline
n = int(input().strip())

########################################
# # Bottom Up

# dp = [0, 1, 2, 3, ]

# for i in range(4, n + 1):
#     dp.append(dp[i-1] + dp[i-2])

# print(dp[n] % 10007)

########################################
# Top Down

dp = {1:1, 2:2, 3:3}
def num_ways(n):
    if dp.get(n) != None:
        return dp.get(n)
    else:
        dp[n] = num_ways(n-1) + num_ways(n-2)
        return dp.get(n)

print(num_ways(n)%10007)
    