########################################
# 23-12-14 (3)
# Bottom up - 다른 사람 코드 참고
import sys
sys_input = sys.stdin.readline
tc = int(sys_input())
numbers = []
for _ in range(tc):
    numbers.append(int(sys_input()))
max_number = max(numbers)
dp = [0, 1, 2, 4, 7] + [0] * max_number

for i in range(5, max_number + 1):
    dp[i] = (dp[i-1]+ dp[i-2]+ dp[i-3])%1_000_000_009


for n in numbers:
    print(dp[n]%1_000_000_009)

########################################
# 23-12-14 (2)
# Top down 시간초과
import sys
sys_input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dp = [-1, 1, 2, 4, 7] + [-1] * 1_000_000

def oneTwoThree(n):
     if (dp[n] >= 0):
          return dp[n]
     dp[n] = (oneTwoThree(n-1) + oneTwoThree(n-2) + oneTwoThree(n-3))%1_000_000_009
     return dp[n]

for _ in range(int(sys_input())):
    n = int(sys_input())
    print(oneTwoThree(n))

########################################
# 23-12-14 (1)
# Bottom up 시간초과
import sys
sys_input = sys.stdin.readline
tc = int(sys_input())

dp = [0, 1, 2, 4, 7] + [0] * 1_000_000

for _ in range(tc):
    n = int(sys_input())
    for i in range(5, n+1):
         dp[i] = (dp[i-1]+ dp[i-2]+ dp[i-3])%1_000_000_009
    print(dp[n]%1_000_000_009)