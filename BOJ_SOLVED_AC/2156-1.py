#
# 24-03-19
# dp[i] : i 째 까지 최적
# dp[i] = max(dp[i-1], wine[i] + wine[i-1] + dp[i-3], wine[i] + dp[i-2])
#

import sys
sys_input = sys.stdin.readline

N = int(sys_input().strip())
wine = []
for _ in range(N):
    wine.append(int(sys_input().strip()))
    
if N == 1:
    print(wine[0])
elif N == 2:
    print(wine[0] + wine[1])
elif N == 3:
    print(max(wine[0] + wine[1], wine[1] + wine[2], wine[2] + wine[0]))
else:
    # 0, 1
    dp1 = [0] * N
    dp1[0] = wine[0]
    dp1[1] = dp1[0] + wine[1]
    dp1[2] = dp1[1]
    for i in range(3, N):
        dp1[i] = max(dp1[i-1], wine[i] + wine[i-1] + dp1[i-3], wine[i] + dp1[i-2])
    
    # 0, 2
    dp2 = [0] * N
    dp2[0] = wine[0]
    dp2[1] = dp2[0]
    dp2[2] = dp2[1] + wine[2]
    for i in range(3, N):
        dp2[i] = max(dp2[i-1], wine[i] + wine[i-1] + dp2[i-3], wine[i] + dp2[i-2])
    
    # 1, 2
    dp3 = [0] * N
    dp3[0] = 0
    dp3[1] = wine[1]
    dp3[2] = dp3[1] + wine[2]
    for i in range(3, N):
        dp3[i] = max(dp3[i-1], wine[i] + wine[i-1] + dp3[i-3], wine[i] + dp3[i-2])

    # print(dp1)
    # print(dp2)
    # print(dp3)
    print(max(dp1[N - 1], dp2[N - 1], dp3[N - 1]))
    
#
# 같은 점화식이지만, 다음 코드는 더 간결하게 풀었음
# https://www.acmicpc.net/source/52895638
# 순회를 3 ~ n + 3 으로 함
#
import sys
N = int(sys.stdin.readline().strip())
wine = [0,0,0]
dp = [0,0,0] + [0] * N
# for _ in range(N):
#     wine.append(int(sys.stdin.readline().strip()))
    
for i in range(3, N + 3):
    wine.append(int(sys.stdin.readline().strip()))
    dp[i] = max(dp[i-1], wine[i] + wine[i-1] + dp[i-3], wine[i] + dp[i-2])

print(dp[N + 2])