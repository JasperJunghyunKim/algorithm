import sys
sys_input = sys.stdin.readline

NUM_TYPES, MAX_CAPA = map(int, sys_input().strip().split())

items = []
for _ in range(NUM_TYPES):
    weight, satisfaction, num_items = map(int, sys_input().strip().split())
    # 아이템 분할
    cnt = 1
    while num_items > 0:

        multiple = min(num_items, cnt)
        items.append((weight * multiple, satisfaction * multiple))
        num_items -= multiple
        cnt *= 2

dp = [0] * (MAX_CAPA + 1)
for weight, satisfaction in items:
    for c in range(MAX_CAPA, weight - 1, -1):
        if c >= weight:
            dp[c] = max(dp[c], satisfaction + dp[c - weight])

print(dp[MAX_CAPA])