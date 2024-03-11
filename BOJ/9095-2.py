#
# 24-03-11 
# Bottom Up, Memoization
#

import sys
n = int(input().strip())

tc = []

for i in range(n):
    tc.append(int(input().strip()))

ans = [0, 1, 2, 4]
max_value = max(tc)

for i in range(4, max_value + 1):
    ans.append(ans[i-1] + ans[i-2] + ans[i-3])

for i in tc:
    print(ans[i])