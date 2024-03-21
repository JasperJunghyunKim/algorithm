import sys
sys_input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(1000**2)

row, col = map(int, sys_input().split(' '))
paint = [list(sys_input().strip()) for _ in range(row)]
pixel_r, pixel_c, color = map(int, sys_input().split(' '))

def bucketfill_bfs(i, j, new_color):
    if new_color == paint[i][j]:
        return
    original_color = paint[i][j]
    next_visit = deque()
    paint[i][j] = new_color
    next_visit.append((i, j))

    while next_visit:
        cur_row, cur_col = next_visit.popleft()
        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            next_row, next_col = cur_row + dr, cur_col + dc
            if 0 <= next_row < row and 0 <= next_col < col:
                if paint[next_row][next_col] == original_color:
                    paint[next_row][next_col] = new_color
                    next_visit.append((next_row, next_col))

def bucketfill_dfs(i, j, new_color):
    original_color = paint[i][j]
    paint[i][j] = new_color
    for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
        if 0 <= i + dr < row and 0 <= j + dc < col:
            if paint[i + dr][j + dc] == original_color:
                bucketfill_dfs(i + dr, j + dc, new_color)
                

bucketfill_bfs(pixel_r, pixel_c, str(color))
# bucketfill_dfs(pixel_r, pixel_c, str(color))

for i in range(row):
    print(*paint[i], sep='')