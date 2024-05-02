#
# @2024-04-27
# 점화식
# 마지막 계단은 무조건 밟아야하는 경우이므로, dp 는 다음과 같이 정의함
# dp : 마지막 계단을 밟을 때, 최대 점수
# dp[i] = max(step[i] + dp[i-2], step[i] + step[i-1] + dp[i-3])
# 즉, i-1를 밟지 않는 경우 / i-2를 밟지 않는 경우 중 최대를 찾으면 됨
#


import sys
sys_input = sys.stdin.readline

N = int(sys_input().strip())
# dp = [0] * (N + 1)
dp_must = [0] * (N + 1)
step = [0] * (N + 1)
for i in range(1, N + 1):
    step[i] = int(sys_input().strip())
if N == 1:
    print(step[1])
    exit()
elif N == 2:
    print(step[1] + step[2])
    exit()
elif N == 3:
    print(max(step[2] + step[3], step[3] + step[1]))
    exit()
# dp[1] = step[1]
dp_must[1] = step[1]
# dp[2] = step[1] + step[2]
dp_must[2] = step[1] + step[2]
# dp[3] = max(step[1] + step[2], step[2] + step[3], step[3] + step[1])
dp_must[3] = max(step[2] + step[3], step[3] + step[1])
for i in range(4, N + 1):
    # dp[i] = max(step[i] + step[i-1] + dp_must[i-3], step[i] + dp_must[i-2], dp_must[i-1])
    dp_must[i] = max(step[i] + step[i-1] + dp_must[i-3], step[i] + dp_must[i-2])
    
# 마지막은 무조건 밟아야 하므로, 점화식 별도 처리
print(dp_must[N])

