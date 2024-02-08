import sys
sys_input = sys.stdin.readline
from collections import deque
size = int(sys_input())
graph = [list(map(int, sys_input().split(' '))) for _ in range(size)]

# MAX HEIGHT
max_height = 0
for i in range(size):
    max_height = max(max_height, max(graph[i]))

def bfs(i, j, height):
    next_visit = deque()
    visited[i][j] = True
    next_visit.append((i,j))
    while next_visit:
        cur_row, cur_col = next_visit.popleft()
        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            next_row, next_col = cur_row + dr, cur_col + dc
            # range
            # not visited
            # safety
            if 0 <= next_row < size and 0 <= next_col < size:
                if visited[next_row][next_col] == False:
                    if graph[next_row][next_col] - height > 0:
                        visited[next_row][next_col] = True
                        next_visit.append((next_row, next_col))

# FIND MAX NUM OF SHELTERS
max_num_safety = 0
for height in range(0, max_height + 1):
    visited = [[False for _ in range(size)] for _ in range(size)]
    num_safety = 0
    for i in range(size):
        for j in range(size):
            if visited[i][j] == False:
                if graph[i][j] - height > 0:
                    num_safety += 1
                    bfs(i, j, height)
    max_num_safety = max(max_num_safety, num_safety)
print(max_num_safety)


# ########################################
# # T1
# ########################################
# import sys
# from collections import deque
# input = sys.stdin.readline

# n = int(input())
# max_altitue = 0
# altitude = []

# for _ in range(n):
#     new_row = list(map(int, input().split(' ')))
#     altitude.append(new_row)
#     for i in new_row:
#         if i > max_altitue:
#             max_altitue = i

# num_safety = [0] * 101

# for level in range(0, max_altitue):
#     visited = [[False for _ in range(n)] for _ in range(n)]
#     to_visit = deque()
#     cnt = 0
#     for i in range(n):
#         for j in range(n):
#             if altitude[i][j] - level > 0 and visited[i][j] == False:
#                 cnt += 1
#                 to_visit.append((i,j))
#                 visited[i][j] = True
#                 while to_visit:
#                     cur_pos = to_visit.popleft()
#                     for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
#                         next_pos = (cur_pos[0] + dx, cur_pos[1] + dy)
#                         if 0 <= next_pos[0] < n and 0 <= next_pos[1] < n:
#                             if altitude[next_pos[0]][next_pos[1]] - level > 0:
#                                 if visited[next_pos[0]][next_pos[1]] == False:
#                                     to_visit.append(next_pos)
#                                     visited[next_pos[0]][next_pos[1]] = True
#     num_safety[level] = cnt

# print(max(num_safety))