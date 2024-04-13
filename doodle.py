import sys
sys_input = sys.stdin.readline

NUM_ITEM, MAX_CAPA = map(int, sys_input().strip().split())
W, V = 0, 1
items = []
for _ in range(NUM_ITEM):
    items.append(tuple(map(int, sys_input().strip().split())))

# # dp 1 차원
# dp = [0] * (MAX_CAPA + 1)
# for i in range(NUM_ITEM):
#     for c in range(MAX_CAPA, -1, -1):
#         if items[i][W] <= c:
#             dp[c] = max(dp[c], items[i][V] + dp[c - items[i][W]])
# print(dp[MAX_CAPA])

# 향상된 DP
items.sort(reverse = True)
promising = {0:0}
for w, v in items:
    tmp = {}
    for v_promising, w_promising in promising.items():
        # 
        new_v = v_promising + v
        new_w = w_promising + w
        if (new_v not in promising or promising[new_v] > new_w) and new_w <= MAX_CAPA:
            tmp[new_v] = new_w
        
    promising.update(tmp)

print(max(promising.keys()))