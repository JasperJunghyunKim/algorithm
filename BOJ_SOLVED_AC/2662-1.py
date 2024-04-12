import sys
sys_input = sys.stdin.readline

TOTAL_INVEST, NUM_COMPANY = map(int, sys_input().strip().split())

# profit[i][c] : i 원을 c 컴퍼니에 투자할 때의 수익 (1 <= i, 1 <= c)
profit = [[0 for _ in range(NUM_COMPANY + 1)]]
for _ in range(TOTAL_INVEST):
    profit.append(list(map(int, sys_input().strip().split())))

max_profit = 0
max_profit_combination = [[[] for _ in range(NUM_COMPANY + 1)] for _ in range(TOTAL_INVEST + 1)]
dp = [[0 for _ in range(NUM_COMPANY + 1)] for _ in range(TOTAL_INVEST + 1)]
for i in range(TOTAL_INVEST + 1):
    dp[i][1] = profit[i][1]
    max_profit_combination[i][1].append(i)

    
for c in range(2, NUM_COMPANY + 1):
    for i in range(TOTAL_INVEST + 1):
        for r in range(i + 1):
            # dp[i][c] = max(dp[i][c], profit[r][c] + dp[i-r][c-1])
            # if dp[i][c] > profit[r][c] + dp[i-r][c-1]:
                # dp[i][c] = dp[i][c]
                # max_profit_combination[i] = max_profit_combination[i]
            # if dp[i][c] > profit[r][c] + dp[i-r][c-1]:
                # max_profit_combination[i].append(0)
            if dp[i][c] <= profit[r][c] + dp[i-r][c-1]:
                dp[i][c] = profit[r][c] + dp[i-r][c-1]
                l = max_profit_combination[i-r][c-1][::]
                # if len(l) == c:
                #     l.pop()
                l.append(r)
                max_profit_combination[i][c] = l
                
print(dp[TOTAL_INVEST][NUM_COMPANY])
print(*max_profit_combination[TOTAL_INVEST][NUM_COMPANY])
            