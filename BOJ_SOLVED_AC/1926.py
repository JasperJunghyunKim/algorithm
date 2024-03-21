########################################
# T2 : BFS
########################################
import sys
sys_input = sys.stdin.readline
from collections import deque

row, col = map(int, sys_input().split(' '))
paper = [list(map(int, sys_input().split(' '))) for _ in range(row)]

def bfs(i, j):
    size_paint = 0
    next_visit = deque()
    paper[i][j] = -1
    next_visit.append((i, j))
    size_paint += 1
    while next_visit:
        cur_row, cur_col = next_visit.popleft()
        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            next_row, next_col = cur_row + dr, cur_col + dc
            if 0 <= next_row < row and 0 <= next_col < col and paper[next_row][next_col] == 1:
                paper[next_row][next_col] = -1
                next_visit.append((next_row, next_col))
                size_paint += 1
    return size_paint
    
size_paint = [0, ]
num_paint = 0
for i in range(row):
    for j in range(col):
        if paper[i][j] == 1:
            num_paint += 1
            size_paint.append(bfs(i,j))

print(num_paint)
print(max(size_paint))

# ########################################
# # T1 : DFS
# ########################################
# import sys
# sys_input = sys.stdin.readline
# sys.setrecursionlimit(500**2)

# row, col = map(int, sys_input().split(' '))
# paper = [list(map(int, sys_input().split(' '))) for _ in range(row)]

# def dfs(i, j):
#     size_paint = 1
#     paper[i][j] = -1
#     for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
#         next_row, next_col = i + dr, j + dc
#         if 0 <= next_row < row and 0 <= next_col < col and paper[next_row][next_col] == 1:
#             size_paint += dfs(next_row, next_col)
#     return size_paint

# num_paints = 0
# size_paint = 0
# for i in range(row):
#     for j in range(col):
#         if paper[i][j] == 1:
#             num_paints += 1
#             size_temp = dfs(i,j)
#             size_paint = size_paint if size_paint > size_temp else size_temp

# print(num_paints)
# print(size_paint)