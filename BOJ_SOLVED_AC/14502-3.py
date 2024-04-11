import sys
from collections import deque
sys_input = sys.stdin.readline
NUM_ROW, NUM_COL = map(int, sys_input().strip().split())
BLANK = 0
WALL = 1
VIRUS = 2
max_safety_size = 0

lab = [list(map(int, sys_input().strip().split())) for _ in range(NUM_ROW)]
virus_position = []
blank_position = []
for r in range(NUM_ROW):
    for c in range(NUM_COL):
        if lab[r][c] == VIRUS: virus_position.append((r,c))
        if lab[r][c] == BLANK: blank_position.append((r,c))
NUM_BLANKS = len(blank_position)

def get_safety():
    contaged = [[False for _ in range(NUM_COL)] for _ in range(NUM_ROW)]
    to_contage = deque(virus_position)
    for v_r, v_c in virus_position:
        contaged[v_r][v_c] = True
    while to_contage:
        cur_r, cur_c = to_contage.popleft()
        for d_r, d_c in [(0,1), (0,-1), (1,0), (-1,0)]:
            next_r, next_c = cur_r + d_r, cur_c + d_c
            if 0 <= next_r < NUM_ROW and 0 <= next_c < NUM_COL:
                if lab[next_r][next_c] == BLANK and not contaged[next_r][next_c]:
                    contaged[next_r][next_c] = True
                    to_contage.append((next_r, next_c))
    
    # calculate safety area
    safety_size = 0
    for r in range(NUM_ROW):
        for c in range(NUM_COL):
            if lab[r][c] == BLANK and not contaged[r][c]: safety_size += 1
                
    return safety_size

def backtrack(num_walls, idx):
    global max_safety_size
    if num_walls == 3:
        safety_size = get_safety()
        max_safety_size = safety_size if safety_size > max_safety_size else max_safety_size
        return
    for i in range(idx, NUM_BLANKS):
        lab[blank_position[i][0]][blank_position[i][1]] = WALL
        # 조합 식 접근
        # file://../algorithms/Permutations_and_Combinations.md
        backtrack(num_walls + 1, i + 1)
        lab[blank_position[i][0]][blank_position[i][1]] = BLANK
        
backtrack(0, 0)
print(max_safety_size)