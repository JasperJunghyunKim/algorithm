#
# 24-03-20 T2
# "2156" 포도주 시식이랑 점화식을 비슷하게 시도했으나, 점화식이 완전히 달랐음
#
import sys
sys_input = sys.stdin.readline

N = int(sys_input().strip())
steps = [0] * (N + 1)
dp = [0] * (N + 1)

for i in range(N):
    steps[i+1] = int(sys_input().strip())
    
dp[1] = steps[1]
if N >= 2:
    dp[2] = steps[1] + steps[2]

# dp[i] : i 째를 밟았을 때의 최대값
# dp[i] = max(steps[i] + steps[i-1] + dp[i-3], steps[i] + dp[i-2])

for i in range(3, N + 1):
    dp[i] = max(steps[i] + steps[i-1] + dp[i-3], steps[i] + dp[i-2])

print(dp[N])

#
# 24-03-20 T1 
# 틀림
# i 번째에서 밟을 경우, 밟지 않을 경우를 고려하여 max 비교한 뒤 dp[i] 에 적용했음
# 그리고 마지막 경우엔 무조건 밟도록 함
# 그러나 점화식은 일반화하여 모든 index 에 적용할 수 있어야 함 -> T2 참고
#

import sys
sys_input = sys.stdin.readline

N = int(sys_input().strip())

#
steps = [0,0,0,0]
dp = [0] * (N + 4)
for i in range(4, N + 4):
    steps.append(int(sys_input().strip()))
    dp[i] = max(steps[i-1] + dp[i-2], steps[i] + steps[i-1] + steps[i-3] + dp[i-4], steps[i] + steps[i-2] + dp[i-3])   
    if i == (N + 3):
        dp[i] = max(steps[i] + steps[i-1] + steps[i-3] + dp[i-4], steps[i] + steps[i-2] + dp[i-3]) 

# print(dp)
print(dp[N+3])