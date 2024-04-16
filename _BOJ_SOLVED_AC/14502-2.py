import sys
sys_input = sys.stdin.readline
from collections import deque

NUM_ROWS, NUM_COLS = map(int, sys_input().strip().split())
original_map = [list(map(int, sys_input().strip().split())) for _ in range(NUM_ROWS)]
empty = []
virus = []
g_shelter = 0
for r in range(NUM_ROWS):
    for c in range(NUM_COLS):
        if original_map[r][c] == 2: virus.append((r,c))
        if original_map[r][c] == 0: empty.append((r,c))
        
def virus_bfs():
    global g_shelter
    temp_map = [i[::] for i in original_map]
    to_visit = deque(virus[::])
    while to_visit:
        cur_r, cur_c = to_visit.popleft()
        for d_r, d_c in [(0,1), (0,-1), (1,0), (-1,0)]:
            next_r, next_c = cur_r + d_r, cur_c + d_c
            if 0 <= next_r < NUM_ROWS and 0 <= next_c < NUM_COLS:
                if temp_map[next_r][next_c] == 0:
                    temp_map[next_r][next_c] = 2
                    to_visit.append((next_r, next_c))
                    
    shelter = 0
    for r in range(NUM_ROWS):
        for c in range(NUM_COLS):
            if temp_map[r][c] == 0:
                shelter += 1
    g_shelter = shelter if shelter > g_shelter else g_shelter
        
def make_wall(total_walls):
    if total_walls == 3:
        virus_bfs()
        return
    for r, c in empty:
        if original_map[r][c] == 0:
            original_map[r][c] = 1
            make_wall(total_walls + 1)
            original_map[r][c] = 0
            
make_wall(0)
print(g_shelter)