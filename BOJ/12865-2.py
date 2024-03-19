#
# 24-03-18
# DP
# 여기서 DP 정의는 capa 에 대하여 item_no 순번까지 고려했을 때, 최적의 해를 의미
# 따라서 dp[capa][item_no] 를 계산할 때, item_no 를 담지 않을 경우엔 dp[capa][item_no - 1] 과 같음 
#
import sys
sys_input = sys.stdin.readline

WEIGHT = 0
VALUE = 1

num_items, max_capa = map(int, sys_input().split())
items = []

# init and sort
for _ in range(num_items):
    items.append(tuple(map(int, sys_input().split())))
# items.sort(key = lambda x : x[1], reverse=True)

dp = [[0 for _ in range(num_items)] for _ in range(max_capa + 1)]

# base value
for capa in range(max_capa + 1):
    if capa >= items[0][0]:
        dp[capa][0] = items[0][1]

for capa in range(1, max_capa + 1):
    for item_no in range(1, num_items):
        # item_no 를 담을 수 있는 경우
        if capa >= items[item_no][WEIGHT]:
            # max(담지 않았을 때, 담았을 때)
            dp[capa][item_no] = max(dp[capa][item_no - 1], items[item_no][VALUE] + dp[capa - items[item_no][WEIGHT]][item_no - 1])
        # 담을 수 없는 경우
        else:
            dp[capa][item_no] = dp[capa][item_no - 1]
        
print(max(dp[max_capa]))