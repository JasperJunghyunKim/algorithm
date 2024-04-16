import sys
sys_input = sys.stdin.readline

N = int(sys_input().strip())
dp = [0] * (N + 1)
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
dp[1] = step[1]
dp_must[1] = step[1]
dp[2] = step[1] + step[2]
dp_must[2] = step[1] + step[2]
dp[3] = max(step[1] + step[2], step[2] + step[3], step[3] + step[1])
dp_must[3] = max(step[2] + step[3], step[3] + step[1])
for i in range(4, N + 1):
    dp[i] = max(step[i] + step[i-1] + dp_must[i-3], step[i] + dp_must[i-2], dp_must[i-1])
    dp_must[i] = max(step[i] + step[i-1] + dp_must[i-3], step[i] + dp_must[i-2])
    
# 마지막은 무조건 밟아야 하므로, 점화식 별도 처리
print(dp_must[N])

