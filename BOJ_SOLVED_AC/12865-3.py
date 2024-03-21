import sys
sys_input = sys.stdin.readline

WEIGHT = 0
VALUE = 1

NUM_ITEMS, MAX_WEIGHT = map(int, sys_input().split(' '))
items = [None] * (NUM_ITEMS + 1)

for i in range(1, NUM_ITEMS + 1):
    items[i] = tuple(map(int, sys_input().split(' ')))
    
dp = [[0 for _ in range(NUM_ITEMS + 1)] for _ in range(MAX_WEIGHT + 1)]
# dp[w][i] : 최대 무게가 w 일 때, i 번째 항목을 고려할 때의 최적 해

# base 조건 초기화 : 1 번째 항목을 고려할 때
for w in range(1, MAX_WEIGHT + 1):
    if w >= items[1][WEIGHT]:
        dp[w][1] = items[1][VALUE]
        

# Bottom Up
# dp[w][i] = max(dp[w][i-1], items[i][VALUE] + dp[w - items[i][WEIGHT]][i-1])
for w in range(1, MAX_WEIGHT + 1):
    for i in range(2, NUM_ITEMS + 1):
        if items[i][WEIGHT] <= w:
            dp[w][i] = max(dp[w][i-1], items[i][VALUE] + dp[w - items[i][WEIGHT]][i-1])
        else:
            dp[w][i] = dp[w][i-1]

print(max(dp[MAX_WEIGHT]))
