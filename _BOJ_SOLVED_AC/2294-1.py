import sys
sys_input = sys.stdin.readline
NUM_TYPES, TARGET_VALUE = map(int, sys_input().strip().split())
coin_set = set()
for _ in range(NUM_TYPES):
    coin_set.add(int(sys_input().strip()))
coin_list = list(coin_set)
coin_list.sort()

# # 아래 코드 시간초과
# #
# # dp[val][coin_idx] : val 을 만들기 위해 coin_idx 번째까지 고려했을 때 최소값
# # 만들 수 없을 경우 inf
# dp = [[float('inf')] * len(coin_list) for _ in range(TARGET_VALUE + 1)]
# for coin in range(len(coin_list)):
#     dp[0][coin] = 0
# for val in range(1, TARGET_VALUE + 1):
#     if val % coin_list[0] == 0:
#         dp[val][0] = val // coin_list[0]
#
# for coin_idx in range(1, len(coin_list)):
#     for val in range(1, TARGET_VALUE + 1):
#         mox = val // coin_list[coin_idx]
#         if mox > 0:
#             # 몫이 1 이상이면, 꼭 사용해야되는 게 몫만큼이 아닐 수 있다
#             # 1 ~ 몫 사이에서 최소를 선택 ... 근데 시간초과
#             for m in range(1, mox + 1):
#                 dp[val][coin_idx] = min(dp[val][coin_idx - 1], mox + dp[val - coin_list[coin_idx] * mox][coin_idx - 1])
#         else:
#             dp[val][coin_idx] = dp[val][coin_idx - 1]
#
# if min(dp[TARGET_VALUE]) == float('inf'):
#     print(-1)
# else:
#     print(min(dp[TARGET_VALUE]))

dp = [float('inf')] * (TARGET_VALUE + 1)
dp[0] = 0
for coin in coin_list:
    for val in range(coin, TARGET_VALUE + 1):
        if dp[val - coin] != float('inf'):
            dp[val] = min(dp[val], 1 + dp[val - coin])

if dp[TARGET_VALUE] == float('inf'):
    print(-1)
else:
    print(dp[TARGET_VALUE])
