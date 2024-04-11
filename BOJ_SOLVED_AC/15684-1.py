#
# 24-04-09
# 실패코드
#

import sys
sys_input = sys.stdin.readline

NUM_COL, NUM_BRIDGE, NUM_ROW = map(int, sys_input().strip().split())
MAP_COL_SIZE = NUM_COL * 2 - 1
MAP_ROW_SIZE = NUM_ROW * 2 - 1
min_bridges = 0

# INIT MAP
ladder_map = [[0 for _ in range(MAP_COL_SIZE)] for _ in range(MAP_ROW_SIZE)]
for c in range(0, MAP_COL_SIZE, 2):
        for r in range(MAP_ROW_SIZE):
            ladder_map[r][c] = 1

for _ in range(NUM_BRIDGE):
    a, b = map(int, sys_input().strip().split())
    ladder_map[a * 2 - 2][b * 2 - 1] = 1

# GET AVAILABLE POSITIONS
positions = []
for r in range(MAP_ROW_SIZE):
    for c in range(MAP_COL_SIZE):
        if not r % 2 and c % 2 and ladder_map[r][c] == 0:
            positions.append((r,c))
LEN_POS = len(positions)

# 
def cheat_available(visited):
    for c in range(0, MAP_COL_SIZE, 2):
        start = c
        end = c
        for r in range(0, MAP_ROW_SIZE, 2):
            if (end + 1 < MAP_COL_SIZE and ladder_map[r][end + 1] == 1) or (r, end + 1) in visited and visited[(r, end + 1)]:
                end += 2
            elif end - 1 >= 0 and ladder_map[r][end - 1] == 1 or (r, end - 1) in visited and visited[(r, end - 1)]:
                end -= 2
        if start != end:
            return False
    return True

#
def promising(r, c, visited):
    if c - 2 >= 0:
        if (r, c - 2) in visited:
            return False
    if c + 2 < MAP_COL_SIZE:
        if (r, c + 2) in visited:
            return False
    if r - 2 >= 0:
        if (r - 2, c) in visited:
            return False
    if r + 2 < MAP_ROW_SIZE:
        if (r + 2, c) in visited:
            return False
    return True

# 
visited = {k:False for k in positions}
def combinations(l, length, r, idx):
    if length == r:
        if cheat_available(visited):
            print(length)
            exit()
        return
    for i in range(idx, LEN_POS):
        x, y = positions[i]
        if promising(x, y, visited):
            visited[(x,y)] = True
            combinations(visited, r, i + 1)
            visited.remove((x,y))

for r in range(0, 4):       
    combinations(dict(), 0, r, 0)
print(-1)