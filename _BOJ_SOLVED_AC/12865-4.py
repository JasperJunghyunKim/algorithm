import sys
sys_input = sys.stdin.readline

NUM_ITEM, MAX_CAPA = map(int, sys_input().strip().split())
W, V = 0, 1
items = []
for _ in range(NUM_ITEM):
    items.append(tuple(map(int, sys_input().strip().split())))

# dp[i][k] : 배낭의 현재 버틸 수 있는 무게가 K 일 때, i 번째 아이템을 결정할 때의 최대 가치
dp = [[0 for _ in range(MAX_CAPA + 1)] for _ in range(NUM_ITEM)]

for k in range(MAX_CAPA + 1):
    dp[0][k] = 0 if k < items[0][W] else items[0][V]

for i in range(1, NUM_ITEM):
    for k in range(MAX_CAPA + 1):
        if items[i][W] <= k:
            dp[i][k] = max(dp[i-1][k], items[i][V] + dp[i-1][k - items[i][W]])
        else:
            dp[i][k] = dp[i-1][k]


max_val = max(dp[NUM_ITEM - 1])
print(max_val)