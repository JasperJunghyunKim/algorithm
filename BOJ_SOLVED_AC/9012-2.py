#
# 24-03-11
#

import sys

n = int(input().strip())

tc = []
stack = []
flag = 0 # 0 : NA, 1 : NO, 2 : YES

for i in range(n):
    tc.append(input().strip())
    
for i in tc:
    flag = 0
    for j in i:
        if j == ")": 
            if len(stack) == 0:
                flag = 1
                break
            stack.pop()
        elif j == "(":
            stack.append("(")
    if flag == 1:
        print("NO")
        while len(stack) != 0: stack.pop()
        continue
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")
    while len(stack) != 0: stack.pop()    