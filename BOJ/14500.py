########################################
# T2 : DFS
########################################
import sys
sys_input = sys.stdin.readline
from collections import deque

row, col = map(int, sys_input().split(' '))
paper = [list(map(int, sys_input().split(' '))) for _ in range(row)]

# BFS & DFS
def max_value_block(x, y, depth, visited):
    visited.append((x, y))
    next_dfs = deque()
    next_bfs = deque()
    next_dfs.append((x, y, 1, visited))
    next_bfs.append((x, y, 1, visited))
    while next_dfs or next_bfs:
        cur_bfs_row, cur_bfs_col, cur_bfs_depth, bfs_visited = next_bfs.popleft()
        cur_dfs_row, cur_dfs_col, cur_dfs_depth, dfs_visited = next_dfs.pop()
        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            next_bfs_row, next_bfs_col = cur_bfs_row + dr, cur_bfs_col + dc
            next_dfs_row, next_dfs_col = cur_dfs_row + dr, cur_dfs_col + dc
            if 0 <= next_bfs_row < row and 0 <= next_bfs_col < col:
                if (next_bfs_row, next_bfs_col) not in visited:
                    
            if 0 <= next_dfs_row < row and 0 <= next_dfs_col < col:
                if (next_dfs_row, next_dfs_col) not in visited:

def dfs(cur_row, cur_col, depth, visited):
    visited.append((cur_row, cur_col))
    if depth == 4:
        cur_val = 0
        for i, j in visited:
            cur_val += paper[i][j]
        return cur_val
    max_value = 0
    for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
        next_row, next_col = cur_row + dr, cur_col + dc
        # in range
        # not visited
        if 0 <= next_row < row and 0 <= next_col < col:
            if (next_row, next_col) not in visited:
                max_value = max(max_value, dfs(next_row, next_col, depth + 1, visited[::]))
    return max_value

max_value = 0
for i in range(row):
    for j in range(col):
        max_value = max(max_value, dfs(i, j, 1, []))
print(max_value)

########################################
# T1 : Brute Force - Linear
########################################
# import sys
# sys_input = sys.stdin.readline

# row, col = map(int, sys_input().split(' '))
# paper = [list(map(int, sys_input().split(' '))) for _ in range(row)]

# # (tetro_height, tetro_width), squares 1~4
# tetromino = [
#         # stick
#         [(1,4), (0,0), (0,1), (0,2), (0,3)],
#         [(4,1), (0,0), (1,0), (2,0), (3,0)],
#         # square
#         [(2,2), (0,0), (1,0), (0,1), (1,1)],
#         # L
#         [(3,2), (0,0), (1,0), (2,0), (2,1)],
#         [(3,2), (0,0), (0,1), (1,1), (2,1)],
#         [(2,3), (1,0), (1,1), (1,2), (0,2)],
#         [(2,3), (0,0), (0,1), (0,2), (1,0)],
#         # L Reversed
#         [(3,2), (0,1), (1,1), (2,1), (2,0)],
#         [(3,2), (0,0), (1,0), (2,0), (0,1)],
#         [(2,3), (0,0), (1,0), (1,1), (1,2)],
#         [(2,3), (0,0), (0,1), (0,2), (1,2)],
#         # 
#         [(3,2), (0,0), (1,0), (1,1), (2,1)],
#         [(2,3), (0,1), (1,1), (1,0), (0,2)],
#         [(3,2), (0,1), (1,1), (1,0), (2,0)],
#         [(2,3), (0,0), (0,1), (1,1), (1,2)],
#         # ㅗ
#         [(3,2), (0,0), (1,0), (2,0), (1,1)],
#         [(2,3), (0,0), (0,1), (0,2), (1,1)],
#         [(3,2), (0,1), (1,0), (1,1), (2,1)],
#         [(2,3), (0,1), (1,0), (1,1), (1,2)]        
#     ]

# # for block in tetromino:
# #     height = block[0][0]
# #     width = block[0][1]
# #     for i in range(height):
# #         for j in range(width):
# #             if (i, j) in block[1:]:
# #                 print('*', end='')
# #             else:
# #                 print('-', end='')
# #         print()
# #     print()

# max_value = 0
# for block in tetromino:
#     for i in range(row - block[0][0] + 1):
#         for j in range(col - block[0][1] + 1):
#             cur_value = 0
#             for k in range(1, 5):
#                 cur_value += paper[i + block[k][0]][j + block[k][1]]
#             max_value = max(max_value, cur_value)
# print(max_value)