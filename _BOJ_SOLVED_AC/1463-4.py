import sys
sys_input = sys.stdin.readline
tc = []
ONE, TWO, THREE = 0, 1, 2
for _ in range(int(sys_input().strip())):
    tc.append(int(sys_input().strip()))
max_val = max(tc)

if max_val < 4:
    for t in tc:
        if t == 1: print(1)
        elif t == 2: print(1)
        elif t == 3: print(3)
else:
    dp = [[0,0,0] for _ in range(max_val + 1)]
    dp[1] = [1,0,0]
    dp[2] = [0,1,0]
    dp[3] = [1,1,1]
    for i in range(4, max_val + 1):
        dp[i][ONE] = (dp[i-1][TWO] + dp[i-1][THREE]) % 1_000_000_009
        dp[i][TWO] = (dp[i-2][THREE] + dp[i-2][ONE]) % 1_000_000_009
        dp[i][THREE] = (dp[i-3][ONE] + dp[i-3][TWO]) % 1_000_000_009
    for t in tc:
        print(sum(dp[t]) % 1_000_000_009)

