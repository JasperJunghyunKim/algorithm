#
# 24-03-15
#

import sys
sys_input = sys.stdin.readline
from collections import deque

box_col, box_row, box_het = map(int, sys_input().split())
box = [[] for _ in range(box_het)]
to_visit = deque()

for het in range(box_het):
    for row in range(box_row):
        tmp = list(map(int,  sys_input().split()))
        box[het].append(tmp)
        for col, tomato in enumerate(tmp):
            if tomato == 1:
                to_visit.append((het, row, col))

while to_visit:
    cur_h, cur_r, cur_c = to_visit.popleft()
    for dh, dr, dc in [(1,0,0), (0,1,0), (0,0,1), (-1,0,0), (0,-1,0), (0,0,-1)]:
        next_h = cur_h + dh
        next_r = cur_r + dr
        next_c = cur_c + dc
        if 0 <= next_h < box_het and 0 <= next_r < box_row and 0 <= next_c < box_col:
            if box[next_h][next_r][next_c] == 0 or box[next_h][next_r][next_c] > box[cur_h][cur_r][cur_c] + 1:
                box[next_h][next_r][next_c] = box[cur_h][cur_r][cur_c] + 1
                to_visit.append((next_h, next_r, next_c))

max_days = 0
for het in range(box_het):
    for row in range(box_row):                 
        for col in range(box_col):
            if box[het][row][col] == 0:
                print(-1)
                exit()
            max_days = max(max_days, box[het][row][col])

print(max_days -1)