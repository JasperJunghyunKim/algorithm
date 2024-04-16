#
# dp[1][NONE] = 1, dp[1][LEFT] = 1, dp[1][RIGHT] = 1
# dp[i][NONE] = dp[i-1][NONE] + dp[i-1][LEFT] + dp[i-1][RIGHT]
# dp[i][LEFT] = dp[i-1][NONE] + dp[i-1][RIGHT] 
# dp[i][RIGHT] = dp[i-1][NONE] + dp[i-1][LEFT] 
#

########################################
# 23-12-14
n = int(input())
cage = [[0 for _ in range(3)] for _ in range(n)]
cage[0][0] = 1 # N = 1 일때 배치하지 않는 경우
cage[0][1] = 1 # N = 1 일때 왼쪽에 배치하는 경우
cage[0][2] = 1 # N = 1 일때 오른쪽에 배치하는 경우
for i in range(1, n):
    cage[i][0] = sum(cage[i-1])%9901
    cage[i][1] = (cage[i-1][0] + cage[i-1][2])%9901
    cage[i][2] = (cage[i-1][0] + cage[i-1][1])%9901
print(sum(cage[n-1])%9901)

########################################
# 23-11-07
# 해설 참조 : https://codingwonny.tistory.com/307
import sys
input = sys.stdin.readline

n = int(input().strip())
dp = [[0,0,0], [1,1,1]]

for i in range(2, n+1):
    if i%2 == 0:
        dp[0][0] = (dp[1][0] + dp[1][1] + dp[1][2])%9901
        dp[0][1] = (dp[1][2] + dp[1][0])%9901
        dp[0][2] = (dp[1][0] + dp[1][1])%9901
    elif i%2 == 1:
        dp[1][0] = (dp[0][0] + dp[0][1] + dp[0][2])%9901
        dp[1][1] = (dp[0][2] + dp[0][0])%9901
        dp[1][2] = (dp[0][0] + dp[0][1])%9901

if n%2 == 0:
    print(sum(dp[0])%9901)
elif n%2 == 1:
    print(sum(dp[1])%9901)