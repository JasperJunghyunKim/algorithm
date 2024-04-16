#
# 24-03-12
#
import sys
sys_input = sys.stdin.readline
num_tc = int(sys_input().strip())
tc = []
for _ in range(num_tc):
    tc.append(int(sys_input().strip()))

max_val = max(tc)

memo = [0] * 1_000_001 
memo[1] = 1
memo[2] = 2
memo[3] = 4
memo[4] = 7

# Bottom Up
# max_val 만큼만 미리 순회해서 시간 단축

for i in range(5, max_val + 1):
    memo[i] = (memo[i-1] + memo[i-2] + memo[i-3]) % 1_000_000_009

for n in tc:
    print(memo[n])

# Top Down - Recursion Error & Time Limit
# setrecursionlimt 시도했으나, 시간 초과 발생
# top down 방식으로는 해결하지 못했음

def dp(n):
    if memo[n] > 0: return memo[n]
    
    memo[n] = (dp(n-1) + dp(n-2) + dp(n-3)) % 1_000_000_009
    return memo[n]

dp(max_val)

for n in tc:
    print(memo[n])