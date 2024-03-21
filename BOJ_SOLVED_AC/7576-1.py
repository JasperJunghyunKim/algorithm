import sys
from collections import deque
input = sys.stdin.readline

# INIT
max_days = 0
m, n = map(int, input().split(' '))
visited = [[-1 for _ in range(m)] for _ in range(n)]
box = []
ripen = deque()
for i in range(n):
    row = list(map(int, input().split(' ')))
    box.append(row)
    for j, v in enumerate(row):
        if v == 1:
            ripen.append((i,j))
            visited[i][j] = 0

# MAIN
while ripen:
    cy, cx = ripen.popleft()
    for dy, dx in [(1,0), (-1,0), (0,1), (0,-1)]:
        ny = dy + cy
        nx = dx + cx
        if 0 <= ny < n and 0 <= nx < m:
            if box[ny][nx] == 0 and visited[ny][nx] == -1:
                ripen.append((ny, nx))
                visited[ny][nx] = visited[cy][cx] + 1

# FIND RESULT
not_available = False
for i in range(n):
    for j in range(m):
        if box[i][j] == 0 and visited[i][j] == -1:
            not_available = True
        max_days = max_days if max_days > visited[i][j] else visited[i][j]
    
if not_available:
    print(-1)
else:
    print(max_days)



# ########################################
# # T1 : 완숙 상태의 토마토Queue 에 대하여 BFS 를 각각 실행하여 '시간초과'가 남
# import sys
# from collections import deque
# input = sys.stdin.readline

# # INIT
# max_days = 0
# m, n = map(int, input().split(' '))
# visited = [[-1 for _ in range(m)] for _ in range(n)]
# box = []
# ripen = []
# for i in range(n):
#     row = list(map(int, input().split(' ')))
#     box.append(row)
#     for j, v in enumerate(row):
#         if v == 1:
#             ripen.append((i,j))

# # BFS
# def bfs(i, j, visited, cnt = 0):
#     to_visit = deque()
#     to_visit.append((i,j))
#     visited[i][j] = cnt
#     while to_visit:
#         cur_pos = to_visit.popleft()
#         cur_cnt = visited[cur_pos[0]][cur_pos[1]]

#         for dy, dx in [(1,0), (-1,0), (0,1), (0,-1)]:
#             ny = cur_pos[0] + dy
#             nx = cur_pos[1] + dx
#             # 1. BOX 범위 이내
#             # 2. not visited OR visited[ny][nx] > cur_cnt + 1
#             # 3. box[ny][nx]
#             if 0 <= ny < n and 0 <= nx < m:
#                 if visited[ny][nx] == -1 or visited[ny][nx] > cur_cnt + 1:
#                     if box[ny][nx] == 0:
#                         to_visit.append((ny, nx))
#                         visited[ny][nx] = cur_cnt + 1


# # MAIN
# for i,j in ripen:
#     bfs(i, j, visited, 0)

# # FIND RESULT
# not_available = False
# for i in range(n):
#     for j in range(m):
#         if box[i][j] == 0 and visited[i][j] == -1:
#             not_available = True
#         max_days = max_days if max_days > visited[i][j] else visited[i][j]
    
# if not_available:
#     print(-1)
# else:
#     print(max_days)
