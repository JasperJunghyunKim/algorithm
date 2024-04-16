#
# 24-03-11
# Top Down, Recursive
# 점화식이 아래와 같이 나오는 이유 : https://jyami.tistory.com/15
#

import sys
n = int(input().strip())

tc = []

for i in range(n):
    tc.append(int(input().strip()))

ans = {1:1, 2:2, 3:4}

def find_ans(n):
    if ans.get(n) == None:
        ans[n] = find_ans(n-1) + find_ans(n-2) + find_ans(n-3)
    return ans.get(n)

for i in tc:
    print(find_ans(i))