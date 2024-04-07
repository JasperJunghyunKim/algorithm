# 1. 바이러스가 존재하는 가장 큰 영역을 선택 -> 만약 두개가 중복된다면 버려
# 2. 바이러스의 상하좌우 인접을 선택
# 3. 

# BRUTE FORCE
import sys
sys_input = sys.stdin.readline
from collections import deque
NUM_ROW, NUM_COL = map(int, sys_input().strip().split())
original_map = [list(map(int, sys_input().strip().split())) for _ in range(NUM_ROW)]
virus = []
blanks = []
max_safety_area = 0
for r in range(NUM_ROW):
    for c in range(NUM_COL):
        if original_map[r][c] == 0: blanks.append((r,c))
        if original_map[r][c] == 2: virus.append((r,c))


def virus_bfs():
    global max_safety_area 
    to_visit = deque(virus)
    visited = [[False for _ in range(NUM_COL)] for _ in range(NUM_ROW)]
    for r, c in virus:
        visited[r][c] = True
    while to_visit:
        cur_r, cur_c = to_visit.popleft()
        for d_r, d_c in [(0,1), (0,-1), (1,0), (-1,0)]:
            next_r, next_c = cur_r + d_r, cur_c + d_c
            if 0 <= next_r < NUM_ROW and 0 <= next_c < NUM_COL:
                if original_map[next_r][next_c] == 0:
                    if visited[next_r][next_c] == False:
                        to_visit.append((next_r, next_c))
                        visited[next_r][next_c] = True
                    
    # find number of 0s 
    safety_area = 0
    for r in range(NUM_ROW):
        for c in range(NUM_COL):
            if original_map[r][c] == 0 and not visited[r][c]:
                safety_area += 1
        
    # MAX
    max_safety_area = safety_area if safety_area > max_safety_area else max_safety_area

    return

def make_wall(n):
    if n == 3:
        # 바이러스틀 퍼트린다
        virus_bfs()
        return

    for r, c in blanks:
        if original_map[r][c] == 0:
            original_map[r][c] = 1
            make_wall(n + 1)
            original_map[r][c] = 0
        

make_wall(0)
print(max_safety_area)
            