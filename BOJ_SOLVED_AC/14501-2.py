import sys
sys_input = sys.stdin.readline

N = int(sys_input().strip())
T = 0
P = 1

# dp[i]][d] : i 째 날에, d 만큼의 상담기간(일)이 남아있을 때 최적해
dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)] 

#
meetings = [None] + [tuple(map(int, sys_input().strip().split())) for _ in range(N)]

# dp[1][d] 초기화
for d in range(N + 1):
    dp[1][d] = 0 if d < meetings[1][T] else meetings[1][P]

# 
for i in range(2, N + 1):
    for d in range(N + 2 - i):
        if meetings[i][T] <= d:
            dp[i][d] = max(dp[i-1][1] + meetings[i][P], dp[i-1][d + 1])
        else:
            dp[i][d] = dp[i-1][d + 1]

print(max(dp[N]))