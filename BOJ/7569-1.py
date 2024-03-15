import sys
from collections import deque
input  = sys.stdin.readline
x, y, z = map(int, input().split())
box = [[] for _ in range(z)]
ripen_queue = list()
unripen_cnt = 0
max_days = 0

# INIT
for i in range(z):
    for j in range(y):
        box[i].append(list(map(int, input().split())))
        for k, v in enumerate(box[i][j]):
            if v == 1:
                ripen_queue.append((i,j,k))
            elif v == 0:
                unripen_cnt += 1

if unripen_cnt == 0:
    print(0)
    exit()

# MAIN
dirs = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
while ripen_queue and unripen_cnt :
    next_ripen_queue = list()
    for cz, cy, cx in ripen_queue:
        for dz, dy, dx in dirs:
            nz = cz + dz
            ny = cy + dy
            nx = cx + dx
            if 0 <= nz < z and 0 <= ny < y and 0 <= nx < x and box[nz][ny][nx] == 0:
                unripen_cnt -= 1
                next_ripen_queue.append((nz,ny,nx))
                box[nz][ny][nx] = 1
    max_days += 1
    ripen_queue = next_ripen_queue

if unripen_cnt > 0:
    print(-1)
else:
    print(max_days)

# ########################################
# # T2 : 통과했지만 불필요한 메모리, 시간
# import sys
# from collections import deque
# input  = sys.stdin.readline


# # INIT
# x, y, z = map(int, input().split())
# box = [[] for _ in range(z)]
# visited = [[[-1 for _ in range(x)] for _ in range(y)] for _ in range(z)]
# ripen_queue = deque()
# unripen_list = list()
# max_days = 0

# for i in range(z):
#     for j in range(y):
#         box[i].append(list(map(int, input().split())))
#         for k, v in enumerate(box[i][j]):
#             if v == 1:
#                 ripen_queue.append((i,j,k))
#                 visited[i][j][k] = 0
#             elif v == 0:
#                 unripen_list.append((i,j,k))
                

# # MAIN - BFS 를 바로 실행
# while ripen_queue:
#     cz, cy, cx = ripen_queue.popleft()
#     for dz, dy, dx in [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]:
#         nz = cz + dz
#         ny = cy + dy
#         nx = cx + dx
#         # 1. 박스 범위 내
#         # 2. not visited or visited days exceeds
#         # 3. 다음 토마토가 첫날에 미숙이었을 경우
#         if 0 <= nz < z and 0 <= ny < y and 0 <= nx < x:
#             if visited[nz][ny][nx] == -1 or visited[nz][ny][nx] > visited[cz][cy][cx] + 1:
#                 if box[nz][ny][nx] == 0:
#                     ripen_queue.append((nz,ny,nx))
#                     visited[nz][ny][nx] = visited[cz][cy][cx] + 1
#                     max_days = max_days if max_days > visited[nz][ny][nx] else visited[nz][ny][nx]

# # FIND RESULT
# not_available = False
# for (i,j,k) in unripen_list:
#     # 첫날에 미숙이었으면서 방문되지 않은 경우
#     if box[i][j][k] == 0 and visited[i][j][k] == -1:
#         not_available = True

# if not_available:
#     print(-1)
# else:
#     print(max_days)
            
# ########################################
# # T1 : 시간 초과 - BFS 너무 많이 실행
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# # INIT
# x, y, height = map(int, input().split(' '))
# box = [[[] for j in range(y)] for i in range(height)]
# ripen_tomatoes = []

# # BOX[height][y][x]
# for i in range(height):
#     for j in range(y):
#         tomatoes = list(map(int, input().split(' ')))
#         box[i][j].extend(tomatoes)
#         for k, v in enumerate(tomatoes):
#             if v == 1:
#                 ripen_tomatoes.append((i,j,k))

# # DFS REC
# def dfs(i,j,k, cnt):
#     visited[i][j][k] = cnt
#     for dz, dy, dx in [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]:
#         nz = i + dz
#         ny = j + dy
#         nx = k + dx
#         # 6개 위치에 대해서
#         # 1. 상자 범위 내 있으면서
#         # 2. 체크된 적 없거나 OR 더 짧은 날짜가 가능하면서
#         # 3. 처음부터 미숙인 경우
#         if 0 <= nz < height and 0 <= ny < y and 0 <= nx < x:
#             if visited[nz][ny][nx] == -1 or visited[nz][ny][nx] > cnt + 1:
#                 if box[nz][ny][nx] == 0:
#                     dfs(nz, ny, nx, cnt + 1)

# # MAIN
# visited = [[[-1 for k in range(x)] for j in range(y)] for i in range(height)]
# # print(box)
# # print(visited)
# for (i,j,k) in ripen_tomatoes:
#     # 처음부터 완숙이면서 DFS를 돌지 않은 경우
#     if box[i][j][k] == 1 and visited[i][j][k] == -1:
#         dfs(i, j, k, 0)

# # DERIVE RESULT
# not_available = False
# max_days = 0
# for i in range(height):
#     for j in range(y):
#         for k in range(x):
#             # 미숙 -> 완숙되지 못한 게 있을 경우
#             if visited[i][j][k] == -1 and box[i][j][k] == 0:
#                 not_available = True
#             if visited[i][j][k] >= 0:
#                 max_days = max_days if max_days > visited[i][j][k] else visited[i][j][k]

# if not_available:
#     print(-1)
# else:
#     print(max_days)