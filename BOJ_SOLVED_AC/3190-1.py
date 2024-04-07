import sys
sys_input = sys.stdin.readline
from collections import deque

# INIT
directions = [(0,1), (1,0), (0,-1), (-1,0)]
time  = 0
cur_r = 0
cur_c = 0
cur_d = 0
snake_dict = {(0,0):True} # O(N)
snake_deque = deque([(0,0)])
apples = dict()
SIZE = int(sys_input().strip())
NUM_APPLES = int(sys_input().strip())
for _ in range(NUM_APPLES):
    r, c  = map(int, sys_input().strip().split())
    apples[(r - 1,c - 1)] = True

NUM_CMD = int(sys_input().strip())
cmd = dict()
for _ in range(NUM_CMD):
    t, c = sys_input().strip().split()
    cmd[int(t)] = c

# 
while True:
    
    # 방향 전환
    if cmd.get(time) == "L":
        cur_d = (cur_d + 3) % 4
    elif cmd.get(time) == "D":
        cur_d = (cur_d + 1) % 4
    
    time += 1
    
    next_r, next_c = cur_r + directions[cur_d][0], cur_c + directions[cur_d][1]
    if next_r < 0 or SIZE <= next_r or next_c < 0 or SIZE <= next_c:
        break
    if (next_r, next_c) in snake_dict:
        break
    if (next_r, next_c) in apples:
        snake_dict[(next_r, next_c)] = True
        snake_deque.append((next_r, next_c))
        apples.pop((next_r, next_c))
    else:
        snake_dict[(next_r, next_c)] = True
        snake_deque.append((next_r, next_c))
        tail_r, tail_c = snake_deque.popleft()
        snake_dict.pop((tail_r, tail_c))

    # cur_head 변경
    cur_r = next_r
    cur_c = next_c

print(time)