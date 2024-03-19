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
        dp1[i] = max(dp1[i-1], wine[i] + wine[i-1] + dp1[i-3], wine[i] + wine[i-2] + dp1[i-3])
    
    # 0, 2
    dp2 = [0] * N
    dp2[0] = wine[0]
    dp2[1] = dp2[0]
    dp2[2] = dp2[1] + wine[2]
    for i in range(3, N):
        dp2[i] = max(dp2[i-1], wine[i] + wine[i-1] + dp2[i-3], wine[i] + wine[i-2] + dp2[i-3])
    
    # 1, 2
    dp3 = [0] * N
    dp3[0] = 0
    dp3[1] = wine[1]
    dp3[2] = dp3[1] + wine[2]
    for i in range(3, N):
        dp3[i] = max(dp3[i-1], wine[i] + wine[i-1] + dp3[i-3], wine[i] + wine[i-2] + dp3[i-3])

print(dp1)
print(dp2)
print(dp3)
print(max(dp1[N - 1], dp2[N - 1], dp3[N - 1]))
    
# DP[i] = max(DP[i-1], wine[i] + wine[i-1] + DP[i-3], wine[i] + wine[i-2] + DP[i-3])