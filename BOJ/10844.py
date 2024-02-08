import sys
n = int(sys.stdin.readline())

dp = [[0,0,0,0,0,0,0,0,0,0], [0,1,1,1,1,1,1,1,1,1], [1,1,2,2,2,2,2,2,2,1]]

for i in range(3,n+1):
    dp.append([dp[i-1][1], dp[i-1][0] + dp[i-1][2], dp[i-1][1] + dp[i-1][3], dp[i-1][2] + dp[i-1][4],dp[i-1][3] + dp[i-1][5],dp[i-1][4] + dp[i-1][6],dp[i-1][5] + dp[i-1][7],dp[i-1][6] + dp[i-1][8],dp[i-1][7] + dp[i-1][9],dp[i-1][8]])

print(sum(dp[n])%1_000_000_000)