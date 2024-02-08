########################################
# 23-12-14
n = int(input())
dp = [(0,0), (1,1), (2, 1)]
for i in range(3, n+1):
    dp.append((dp[i-1][0] + dp[i-1][1], dp[i-1][0]))
print(dp[n][1])

########################################
# 23-11
from sys import stdin
n = int(stdin.readline())

zero = [0,1,2,3]
one = [0,1,1,2]

for i in range(4, n+1):
    zero.append(zero[i-1] + one[i-1])
    one.append(zero[i-1])

print(one[n])