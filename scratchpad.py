import sys
sys_input = sys.stdin.readline
NUM_CATEGORY, MAX_CAPA = map(int, sys_input().strip().split())
WEIGHT = 0
SATISFACTION = 1
items = []
for _ in range(NUM_CATEGORY):
    weight, satisfaction, quantity = map(int, sys_input().strip().split())
    q = 1
    while quantity - q > 0:
        items.append((weight * q, satisfaction * q))
        quantity -= q
        q *= 2
    if quantity > 0:
        items.append((weight * quantity, satisfaction * quantity))

# dp[C][I] : C CAPA 일 때, I 아이템까지 선택한 최대 만족도 -> 1차원으로
dp = [0 for _ in range(MAX_CAPA + 1)]\

def find_max(dp):
    for i in range(len(items)):
        for c in range(MAX_CAPA, -1, -1):
            if c >= items[i][WEIGHT]:
                dp[c] = max(dp[c], items[i][SATISFACTION] + dp[c - items[i][WEIGHT]])
    return dp[MAX_CAPA]

print(find_max(dp))


###
