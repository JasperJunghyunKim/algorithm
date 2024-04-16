#
# 24-03-11
#

import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    ps = input().strip()
    check_vps = []
    for j in ps:
        if j == '(':
            check_vps.append(j)
        elif j == ')':
            if len(check_vps) == 0:
                print('NO')
                break
            check_vps.pop()
    else:
        if len(check_vps) != 0:
            print('NO')
        else:
             print('YES')

