#
# 24-03-15
#

import sys
sys_input = sys.stdin.readline
from collections import deque

# init input
num_col, num_row = map(int, sys_input().split())
tomato = []
to_visit = deque()

for _ in range(num_row):
    tomato.append(list(map(int, sys_input().split())))
    
for row in range(num_row):
    for col in range(num_col):
        if tomato[row][col] == 1: to_visit.append((row, col))
       
# bfs 
while to_visit:
    cur_row, cur_col = to_visit.popleft()
    for d_c, d_r in [(0,1), (1,0), (0, -1), (-1,0)]:
        next_col = cur_col + d_c
        next_row = cur_row + d_r
        # if next_col < 0 or num_col <= next_col or next_row < 0 or num_row <= next_row:
        #     continue
        # if tomato[next_row][next_col] == -1:
        #     continue
        # if tomato[next_row][next_col] == 0 or tomato[next_row][next_col] > tomato[cur_row][cur_col] + 1:
        #     to_visit.append((next_row, next_col))
        #     tomato[next_row][next_col] = tomato[cur_row][cur_col] + 1
        if 0 <= next_row < num_row and 0 <= next_col < num_col:
            if tomato[next_row][next_col] == 0 or tomato[next_row][next_col] > tomato[cur_row][cur_col] + 1:
                to_visit.append((next_row, next_col))
                tomato[next_row][next_col] = tomato[cur_row][cur_col] + 1

# find
unripen = False
max_days = 0
for y in range(num_row):
    for x in range(num_col):
        if tomato[y][x] == 0:
            print(-1)
            exit()
        max_days = max(max_days, tomato[y][x])

print(max_days - 1)