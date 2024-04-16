import sys
sys_input = sys.stdin.readline
from collections import deque

SIZE, NUM_COLORS = map(int, sys_input().split())
block_map = [list(map(int, sys_input().split())) for _ in range(SIZE)]
g_largest_block_group = dict()
g_total_point = 0

# BLACK -1
# RBOW 0
# NORMAL 1 ~ N
# EMPTY -2

def find_largest_group():
    global g_largest_block_group
    g_largest_block_group = dict()
    lgst_size = 0
    lgst_num_rainbow = 0
    lgst_norm = tuple()
    lgst_block_group = dict()
    
    # visited = [[False for _ in range(SIZE)] for _ in range(SIZE)]
    
    for r in range(SIZE):
        for c in range(SIZE):
            
            if block_map[r][c] == -1 or block_map[r][c] == 0 or block_map[r][c] == -2: continue
            
            block_group = {(r,c): True}
            next_visit = deque([(r,c)])
            num_rainbows = 0
            while next_visit:
                cur_r, cur_c = next_visit.popleft()
                for d_r, d_c in [(0,1), (0,-1), (1,0), (-1,0)]:
                    next_r, next_c = cur_r + d_r, cur_c + d_c
                    # 1. next coord in range
                    # 2. next coord color / same or rainbow 
                    # 3. next coord not visited
                    if 0 <= next_r < SIZE and 0 <= next_c < SIZE:
                        if block_map[next_r][next_c] == block_map[r][c] or block_map[next_r][next_c] == 0:
                            if (next_r, next_c) not in block_group:
                                if block_map[next_r][next_c] == 0:
                                    num_rainbows += 1
                                block_group[(next_r, next_c)] = True
                                next_visit.append((next_r, next_c))
            norm_block = [k for k, v in block_group.items() if v != 0]
            norm_block = min(norm_block)
            
            if len(block_group) <= 1:
                continue
            # check if this is 'new' largest group
            if len(block_group) > lgst_size:
                lgst_size = len(block_group)
                lgst_num_rainbow = num_rainbows
                lgst_norm = norm_block
                lgst_block_group = {k:v for k, v in block_group.items()}
            elif len(block_group) == lgst_size:
                if num_rainbows > lgst_num_rainbow:
                    lgst_num_rainbow = num_rainbows
                    lgst_norm = norm_block
                    lgst_block_group = {k:v for k, v in block_group.items()}
            elif len(block_group) == lgst_size and num_rainbows == lgst_num_rainbow:
                if lgst_norm < norm_block:
                    lgst_norm = norm_block
                    lgst_block_group = {k:v for k, v in block_group.items()}

        g_largest_block_group = {k: v for k, v in lgst_block_group.items()}     
    

def remove_and_point():
    global g_total_point
    for r, c in g_largest_block_group.keys():
        block_map[r][c] = -2
    g_total_point += len(g_largest_block_group) ** 2


def gravity():
    for r in range(SIZE -1, -1, -1):
        for c in range(SIZE):
            if block_map[r][c] == -2:
                for i in range(1, SIZE):
                    next_r = r - i
                    if 0 <= next_r:
                        if block_map[next_r][c] == -2: continue
                        elif block_map[next_r][c] == -1: break
                        else:
                            block_map[r][c] = block_map[next_r][c]
                            block_map[next_r][c] = -2
                            break
                            
                            

# 반시계 90도
def rotate():
    global block_map
    temp_map = [[] for _ in range(SIZE)]
    idx = 0
    for c in range(SIZE-1, -1, -1):
        temp_map[idx] = [block_map[r][c] for r in range(SIZE)]
        idx += 1
    block_map = temp_map[::]
            


while True:
    find_largest_group()
    if len(g_largest_block_group) <= 1:break
    remove_and_point()
    gravity()
    rotate()
    gravity()
print(g_total_point)