#
# BFS

import sys
from collections import deque
sys_input = sys.stdin.readline

NUM_ROWS, NUM_COLS = map(int, sys_input().split())
HOLE_ROW = None
HOLE_COL = None
marvel_map = [list(sys_input().strip()) for _ in range(NUM_ROWS)]

def get_next_moves(cur_red_row, cur_red_col, cur_blue_row, cur_blue_col):
    next_marvels = []
    
    for direction, (dr, dc) in enumerate([(0,-1), (0,1), (-1,0), (1,0)]):
        
        next_red_r = cur_red_row
        next_red_c = cur_red_col
        next_blue_r = cur_blue_row
        next_blue_c = cur_blue_col
        
        while marvel_map[next_red_r + dr][next_red_c + dc] != '#':
            next_red_r += dr
            next_red_c += dc
            if marvel_map[next_red_r][next_red_c] == 'O':
                next_red_r = -1
                next_red_c = -1
                break
        
        while marvel_map[next_blue_r + dr][next_blue_c + dc] != '#':
            next_blue_r += dr
            next_blue_c += dc
            if marvel_map[next_blue_r][next_blue_c] == 'O':
                next_blue_r = -1
                next_blue_c = -1
                break

        # 상하좌우 시 최종 도달 좌표가 같을 경우 / 단, HOLE 인 경우는 제외
        if next_red_r == next_blue_r and next_red_c == next_blue_c:
            if next_red_r != -1 and next_red_c != -1:
                # LEFT
                if direction == 0:
                    if cur_red_col < cur_blue_col:
                        next_blue_c += 1
                    elif cur_blue_col < cur_red_col:
                        next_red_c += 1
                # RIGHT
                elif direction == 1:
                    if cur_red_col < cur_blue_col:
                        next_red_c -= 1
                    elif cur_blue_col < cur_red_col:
                        next_blue_c -= 1    
                # UP
                elif direction == 2:
                    if cur_red_row < cur_blue_row:
                        next_blue_r += 1
                    elif cur_blue_row < cur_red_row:
                        next_red_r += 1
                
                # DOWN
                elif direction == 3:
                    if cur_red_row < cur_blue_row:
                        next_red_r -= 1
                    elif cur_blue_row < cur_red_row:
                        next_blue_r -= 1

        next_marvels.append((next_red_r, next_red_c, next_blue_r, next_blue_c))    
    
    return next_marvels
    
# find Red, Blue, Hole
for r in range(NUM_ROWS):
    for c in range(NUM_COLS):
        if marvel_map[r][c] == 'R':
            red_start_row = r
            red_start_col = c
        elif marvel_map[r][c] == 'B':
            blue_start_row = r
            blue_start_col = c
        elif marvel_map[r][c] == 'O':
            HOLE_ROW = r
            HOLE_COL = c

# R, B
visited = [(red_start_row, red_start_col, blue_start_row, blue_start_col)]
to_visit = deque([(red_start_row, red_start_col, blue_start_row, blue_start_col, 0)])

while to_visit:
    cur_red_row, cur_red_col, cur_blue_row, cur_blue_col, cur_moves = to_visit.popleft()
    
    # 조작 횟수 초과
    if cur_moves == 11:
        continue
    
    # 둘 다 빠진 경우
    if (cur_red_row, cur_red_col) == (-1, -1) and (cur_blue_row, cur_blue_col) == (-1, -1):
        continue
    
    # RED 만 빠진 경우
    elif (cur_red_row, cur_red_col) == (-1, -1) and (cur_blue_row, cur_blue_col) != (-1, -1):       
        print(cur_moves)
        break
    
    # 다음 위치
    for next_red_row, next_red_col, next_blue_row, next_blue_col in get_next_moves(cur_red_row, cur_red_col, cur_blue_row, cur_blue_col):
        if (next_red_row, next_red_col, next_blue_row, next_blue_col) not in visited:
            visited.append((next_red_row, next_red_col, next_blue_row, next_blue_col))
            to_visit.append((next_red_row, next_red_col, next_blue_row, next_blue_col, cur_moves + 1))
else:
    print(-1)
    