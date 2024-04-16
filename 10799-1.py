import sys
from collections import deque
sys_input = sys.stdin.readline

LASER = list(sys_input().strip())
LEN_CMD = len(LASER)


# 
# T4
#
depth_stack = 0
num_parts = 0
for idx in range(LEN_CMD):
    if LASER[idx] == "(":
        # 레이저라면 -> 인덱스 하나씩 증가
        if LASER[idx + 1] == ")":
            num_parts += depth_stack
        # 막대기의 시작
        else:
            depth_stack += 1
    elif LASER[idx] == ")":
        # 레이저라면
        if LASER[idx - 1] == "(":
            continue
        # 막대기가 끝
        else:
            num_parts += 1
            depth_stack -= 1
print(num_parts)


#
# T2
#
stack = []
num_parts = 0
for idx, cmd in enumerate(LASER):
    if cmd == "(":
        # 레이저라면
        if LASER[idx + 1] == ")":
            # stack = list(map(lambda x: x+1, stack))
            for i in range(len(stack)):
                stack[i] += 1
        # 막대기의 시작
        else:
            stack.append(1)
    elif cmd == ")":
        # 레이저라면
        if LASER[idx - 1] == "(":
            continue
        # 막대기가 끝
        else:
            num_parts += stack.pop()

print(num_parts)
            