import sys
sys_input = sys.stdin.readline
from collections import deque
import math

NUM_ROW, NUM_COL, TEST_TEMP = map(int, sys_input().split())
test_coord = []
warmer = [] # r, c, d 

# init room, wall
room = [list(map(int, sys_input().split())) for _ in range(NUM_ROW)]
wall = []
    
# init test_coordinates, warmer locations
for r in range(NUM_ROW):
    for c in range(NUM_COL):
        if room[r][c] == 5:
            test_coord.append((r,c))
        elif 1 <= room[r][c] <= 4:
            warmer.append((r,c,room[r][c]))
        room[r][c] = 0

# init wall
NUM_WALL = int(sys_input())
for _ in range(NUM_WALL):
    r, c, direction = map(int, sys_input().split())
    r -= 1
    c -= 1
    if direction == 0:
        wall.append((r - 0.5, c))
    elif direction == 1:
        wall.append((r, c + 0.5))
        
        
# 1. RIGHT 2. LEFT 3. UP 4. DOWN
# increase temperature
def run_warmer(warmer_row, warmer_col, warmer_d):
    
    first_heat = [None, (0,1), (0,-1), (-1,0), (1,0)]
    
    to_visit = deque()
    visited = []
    first_heat_row = warmer_row + first_heat[warmer_d][0]
    first_heat_col = warmer_col + first_heat[warmer_d][1]
    if 0 <= first_heat_row < NUM_ROW and 0 <= first_heat_col < NUM_COL:
        to_visit.append((first_heat_row, first_heat_col, 5))
        visited.append((first_heat_row, first_heat_col))
        room[first_heat_row][first_heat_col] += 5
    while to_visit:
        cur_r, cur_c, cur_dt = to_visit.popleft()
        
        # RIGHT
        if warmer_d == 1:
            for k, (dr, dc) in enumerate([(-1, 1), (0, 1), (1, 1)]):
                next_r, next_c, next_dt = cur_r + dr, cur_c + dc, cur_dt - 1
                if 0 <= next_r < NUM_ROW and 0 <= next_c < NUM_COL and next_dt >= 1 and (next_r, next_c) not in visited:
                    n = False
                    # RIGHT UP, RIGHT, RIGHT DOWN
                    if k == 0 and (cur_r - 0.5, cur_c) not in wall and (cur_r - 1, cur_c + 0.5) not in wall: n = True
                    elif k == 1 and (cur_r, cur_c + 0.5) not in wall: n = True
                    elif k == 2 and (cur_r + 0.5, cur_c) not in wall and (cur_r + 1, cur_c + 0.5) not in wall: n = True
                    
                    if n:
                        to_visit.append((next_r, next_c, next_dt))
                        room[next_r][next_c] += next_dt
                        visited.append((next_r, next_c))
        
        # LEFT
        if warmer_d == 2:
            for k, (dr, dc) in enumerate([(-1, -1), (0, -1), (1, -1)]):
                next_r, next_c, next_dt = cur_r + dr, cur_c + dc, cur_dt - 1
                if 0 <= next_r < NUM_ROW and 0 <= next_c < NUM_COL and next_dt >= 1 and (next_r, next_c) not in visited:
                    n = False
                    # LEFT UP, LEFT, LEFT DOWN
                    if k == 0 and (cur_r - 0.5, cur_c) not in wall and (cur_r - 1, cur_c - 0.5) not in wall: n = True
                    elif k == 1 and (cur_r, cur_c - 0.5) not in wall: n = True                 
                    elif k == 2 and (cur_r + 0.5, cur_c) not in wall and (cur_r + 1, cur_c - 0.5) not in wall: n = True
                    
                    if n:
                        to_visit.append((next_r, next_c, next_dt))
                        room[next_r][next_c] += next_dt
                        visited.append((next_r, next_c))

                
        # UP    
        if warmer_d == 3:
            for k, (dr, dc) in enumerate([(-1, -1), (-1, 0), (-1, 1)]):
                next_r, next_c, next_dt = cur_r + dr, cur_c + dc, cur_dt - 1
                if 0 <= next_r < NUM_ROW and 0 <= next_c < NUM_COL and next_dt >= 1 and (next_r, next_c) not in visited:
                    n = False
                    # UP LEFT, UP, UP RIGHT
                    if k == 0 and (cur_r, cur_c - 0.5) not in wall and (cur_r - 0.5, cur_c - 1) not in wall: n = True
                    elif k == 1 and (cur_r - 0.5, cur_c) not in wall: n = True
                    elif k == 2 and (cur_r, cur_c + 0.5) not in wall and (cur_r - 0.5, cur_c + 1) not in wall: n = True
                    
                    if n:
                        to_visit.append((next_r, next_c, next_dt))
                        room[next_r][next_c] += next_dt
                        visited.append((next_r, next_c))

        
        # DOWN
        if warmer_d == 4:
            for k, (dr, dc) in enumerate([(1, -1), (1, 0), (1, 1)]):
                next_r, next_c, next_dt = cur_r + dr, cur_c + dc, cur_dt - 1
                if 0 <= next_r < NUM_ROW and 0 <= next_c < NUM_COL and next_dt >= 1 and (next_r, next_c) not in visited:
                    n = False
                    # DOWN LEFT, DOWN, DOWN RIGHT
                    if k == 0 and (cur_r, cur_c - 0.5) not in wall and (cur_r + 0.5, cur_c - 1) not in wall: n = True
                    elif k == 1 and (cur_r + 0.5, cur_c) not in wall: n = True
                    elif k == 2 and (cur_r, cur_c + 0.5) not in wall and (cur_r + 0.5, cur_c + 1) not in wall: n = True
                    
                    if n:
                        to_visit.append((next_r, next_c, next_dt))
                        room[next_r][next_c] += next_dt
                        visited.append((next_r, next_c))

def mix_temperature():
    dt_map = [[[] for _ in range(NUM_COL)] for _ in range(NUM_ROW)]
    for r in range(NUM_ROW):
        for c in range(NUM_COL):
            cur_pos_temp = room[r][c]
            # mix RIGHT
            if c + 1 < NUM_COL and (r, c + 0.5) not in wall:
                right_pos_temp = room[r][c + 1]
                diff = math.floor(abs(cur_pos_temp - right_pos_temp)/4)
                if cur_pos_temp > right_pos_temp:
                    dt_map[r][c].append(-diff)
                    dt_map[r][c + 1].append(diff)
                elif cur_pos_temp < right_pos_temp:
                    dt_map[r][c].append(diff)
                    dt_map[r][c + 1].append(-diff)
            # mix BELOW
            if r + 1 < NUM_ROW and (r + 0.5, c) not in wall:
                down_pos_temp = room[r + 1][c]
                diff = math.floor(abs(cur_pos_temp - down_pos_temp)/4)
                if cur_pos_temp > down_pos_temp:
                    dt_map[r][c].append(-diff)
                    dt_map[r + 1][c].append(diff)
                elif cur_pos_temp < down_pos_temp:
                    dt_map[r][c].append(diff)
                    dt_map[r + 1][c].append(-diff)
    
    # 변화량을 일괄 적용
    for r in range(NUM_ROW):
        for c in range(NUM_COL):
            for d in dt_map[r][c]:
                room[r][c] += d
                    
def edge_minus_one():
    for r in range(NUM_ROW):
        for c in range(NUM_COL):
            if r == 0 or r == NUM_ROW - 1 or c == 0 or c == NUM_COL - 1:
                if room[r][c] >= 1:
                    room[r][c] -= 1
    
test_qualified = False
eat_choco = 0      
while test_qualified == False:
    
    if eat_choco > 100:
        print(101)
        break
    
    # 1
    for r, c, d in warmer:
        run_warmer(r, c, d)
        
    # 2
    mix_temperature()
    
    # 3
    edge_minus_one()
    
    # 4
    eat_choco += 1
    
    # 5
    all_above = True
    for r, c in test_coord:
        if room[r][c] < TEST_TEMP:
            all_above = False
    if all_above == False:
        test_qualified = False
    else:
        test_qualified = True
else:
    print(eat_choco)

# print(*room, sep="\n")

# mix_temperature()

# print()

# print(*room, sep="\n")

# edge_minus_one()
# print()

# print(*room, sep="\n")
