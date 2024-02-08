########################################
# 23-12-14
from collections import deque
n = int(input())
now  = 1
stack = deque()
find = True
result = []
for _ in range(n):
    num = int(input())
    while now <= n:
        stack.append(now)
        now += 1
        result.append("+")
    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        find = False
if find == False:
    print("NO")
else:
    print(*result, sep="\n")
    

########################################
# 23-11
import sys
input = sys.stdin.readline

n = int(input())
sequence = [0, ]
my_stack = []
my_operator = []
cur_index = 1
cur_val = 1
for i in range(n):
    sequence.append(int(input()))

while cur_index < n + 1:
    if len(my_stack) == 0:
        my_stack.append(cur_val)
        my_operator.append('+')
        cur_val += 1
    else:
        if my_stack[-1] == sequence[cur_index]:
            my_stack.pop()
            my_operator.append('-')
            cur_index += 1
        else:
            if(cur_val == n + 1):
                break
            my_stack.append(cur_val)
            my_operator.append('+')
            cur_val += 1

while not len(my_stack) == 0:
    if my_stack[-1] == sequence[cur_index]:
        my_stack.pop()
        my_operator.append('-')
        cur_index += 1
    else:
        break

# result
if len(my_stack) == 0:
    for i in my_operator:
        print(i)
else:
    print('NO')