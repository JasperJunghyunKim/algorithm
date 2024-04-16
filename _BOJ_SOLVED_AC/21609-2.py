BLACK = -1
RAINBOW = 0
EMPTY = -2
import sys
sys_input = sys.stdin.readline
from collections import deque

SIZE, NUM_COLORS = map(int, sys_input().split())
block_map = [list(map(int, sys_input().split())) for _ in range(SIZE)]
g_largest_block = dict()
g_total_point = 0


def find_largest_group():
    global g_largest_block
    g_largest_block = dict()
    
    for r in range(SIZE):
        for c in range(SIZE):
            if block_map[r][c] == BLACK or block_map[r][c] == RAINBOW or block_map[r][c] == EMPTY:
                continue
            
            # for each normal block, do flood fill
            block_color = block_map[r][c]
            visited = {(r,c): block_color}
            to_visit = deque([(r,c)])
            while to_visit:
                cur_r, cur_c = to_visit.popleft()
                for d_r, d_c in [(0,1), (0,-1), (1,0), (-1,0)]:
                    next_r, next_c = cur_r + d_r, cur_c + d_c
                    # for each next_block ... if 
                    # 1. in range
                    # 2. not visited
                    # 3. same color || rainbow
                    if 0 <= next_r < SIZE and 0 <= next_c < SIZE:
                        if (next_r, next_c) not in visited:
                            if block_map[next_r][next_c] == block_color or block_map[next_r][next_c] == RAINBOW:
                                visited[(next_r, next_c)] = block_map[next_r][next_c]
                                to_visit.append((next_r, next_c))

            # size 1 is not a group
            if len(visited) <= 1:
                continue
            
            # compare temp vs. g_largest_block
            if len(visited) > len(g_largest_block):
                g_largest_block = {k:v for k,v in visited.items()}
            elif len(visited) == len(g_largest_block):
                if list(visited.values()).count(RAINBOW) > list(g_largest_block.values()).count(RAINBOW):
                    g_largest_block = {k:v for k,v in visited.items()}
            elif len(visited) == len(g_largest_block):
                if list(visited.values()).count(RAINBOW) == list(g_largest_block.values()).count(RAINBOW):
                    temp_norm = min([k for k, v in visited.items() if v != RAINBOW])
                    largest_norm = min([k for k, v in g_largest_block.items() if v != RAINBOW])
                    if temp_norm > largest_norm:
                        g_largest_block = {k:v for k,v in visited.items()}

def remove_and_point():
    global g_total_point
    for r, c in g_largest_block.keys():
        block_map[r][c] = EMPTY
    g_total_point += len(g_largest_block) ** 2
    
def gravity():
    for cur_r in range(SIZE - 1, -1, -1):
        for cur_c in range(SIZE):
            if block_map[cur_r][cur_c] == EMPTY:
                for d_r in range(1, SIZE):
                    next_r = cur_r - d_r
                    # in range
                    if next_r >= 0:
                        if block_map[next_r][cur_c] == EMPTY: continue
                        elif block_map[next_r][cur_c] == BLACK: break
                        else:
                            block_map[cur_r][cur_c] = block_map[next_r][cur_c]
                            block_map[next_r][cur_c] = EMPTY
                            break
# 90 C-Clockwise
def rotate():
    global block_map
    rotated_map = [[] for _ in range(SIZE)]
    idx = 0
    for c in range(SIZE - 1, -1, -1):
        rotated_map[idx] = [block_map[r][c] for r in range(SIZE)]
        idx += 1
    block_map = rotated_map[::]
        
while True:
    find_largest_group()
    if len(g_largest_block) <= 1:
        break
    remove_and_point()
    gravity()
    rotate()
    gravity()

print(g_total_point)
    