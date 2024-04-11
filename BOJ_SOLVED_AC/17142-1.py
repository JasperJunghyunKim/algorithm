import sys
sys_input = sys.stdin.readline
from collections import deque
SIZE, NUM_ACTIVE = map(int, sys_input().strip().split())
lab = [list(map(int, sys_input().strip().split())) for _ in range(SIZE)]
g_min_time = float('inf')

virus_positions = []
for r in range(SIZE):
    for c in range(SIZE):
        if lab[r][c] == 2: virus_positions.append((r,c))
NUM_VIRUS = len(virus_positions)
is_active_virus = [False for _ in range(NUM_VIRUS)]



def bfs_virus():
    
    num_blanks = 0
    for r in range(SIZE):
        for c in range(SIZE):
            if lab[r][c] == 0:
                num_blanks += 1
    
    duration = 0
    to_contage = deque()
    contaged = [[False for _ in range(SIZE)] for _ in range(SIZE)]
    deactive_virus = dict()
    for i in range(NUM_VIRUS):
        if is_active_virus[i]: 
            v_r, v_c = virus_positions[i]
            to_contage.append((v_r, v_c, 1))
            contaged[v_r][v_c] = True
        else:
            deactive_virus[virus_positions[i]] = True


    while to_contage and num_blanks:
        cur_r, cur_c, cur_t = to_contage.popleft()
        duration = cur_t if cur_t > duration else duration
        for d_r, d_c in [(0,1), (0,-1), (1,0), (-1,0)]:
            next_r, next_c = cur_r + d_r, cur_c + d_c
            if 0 <= next_r < SIZE and 0 <= next_c < SIZE:
                # 빈 칸이라면 바로 감염
                if lab[next_r][next_c] == 0 and not contaged[next_r][next_c]:
                    to_contage.append((next_r, next_c, cur_t + 1))
                    contaged[next_r][next_c] = True
                    num_blanks -= 1
                # 비활성화 바이러스면 -> 활성화
                elif lab[next_r][next_c] == 2 and (next_r, next_c) in deactive_virus:
                    to_contage.append((next_r, next_c, cur_t + 1))
                    contaged[next_r][next_c] = True
                    deactive_virus.pop((next_r, next_c))

    
    is_all_contaged = True
    for r in range(SIZE):
        for c in range(SIZE):
            if lab[r][c] == 0 and contaged[r][c] == False: is_all_contaged = False
    
    
    return duration if is_all_contaged else float('inf')
                    

def backtrack(num_active_virus, idx):
    global g_min_time
    if num_active_virus == NUM_ACTIVE:
        duration = bfs_virus()
        g_min_time = duration if duration < g_min_time else g_min_time
        return
    
    for i in range(idx, NUM_VIRUS):
        is_active_virus[i] = True
        backtrack(num_active_virus + 1, i + 1)
        is_active_virus[i] = False

        
        
backtrack(0, 0)
if g_min_time == float('inf'):
    print(-1)
else:
    print(g_min_time)