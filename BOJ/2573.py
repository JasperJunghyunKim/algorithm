import sys
from collections import deque
input = sys.stdin.readline
map_x, map_y = map(int, input().split(' '))

# INIT
sea = []
glacier = []
for i in range(map_x):
    sea.append(list(map(int, input().split(' '))))

for i in range(map_x):
    for j in range(map_y):
        if sea[i][j] != 0:
            glacier.append((i, j))

# FUNC
def find_melt(i, j):
    cnt = 0
    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
        next_pos = (i + dx, j + dy)
        if 0 <= next_pos[0] < map_x and 0 <= next_pos[1] < map_y:
            if sea[next_pos[0]][next_pos[1]] <= 0:
                cnt += 1
    return ((i, j), cnt)

def bfs(i, j, visited, to_visit):
    to_visit.append((i, j))
    visited[i][j] = True
    while to_visit:
        cur_pos = to_visit.popleft()
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            next_pos = (cur_pos[0] + dx, cur_pos[1] + dy)
            if 0 <= next_pos[0] < map_x and 0 <= next_pos[1] < map_y:
                if sea[next_pos[0]][next_pos[1]] > 0 and visited[next_pos[0]][next_pos[1]] == False:
                    to_visit.append(next_pos)
                    visited[next_pos[0]][next_pos[1]] = True


# MAIN
num_years = 0
while True:
    all_glaciers_melted = True
    num_glacier = 0
    visited = [[False for _ in range(map_y)] for _ in range(map_x)]
    to_visit = deque()
    to_melt = []
    del_glacier = []
    # BFS : Find number of Glaciers
    for (i,j) in glacier:
        to_melt.append(find_melt(i, j))
        if visited[i][j] == False:
            all_glaciers_melted = False
            num_glacier += 1
            bfs(i, j, visited, to_visit)
    # Break Point 1 : If num_glaciers > 2, print years
    if num_glacier >= 2:
        print(num_years)
        break
    # Break Point 2 : If glaciers all melted, print 0
    if all_glaciers_melted :
        print(0)
        break
    # Melt ice
    for ((i, j), n) in to_melt:
        sea[i][j] -= n
        if sea[i][j] <= 0:
            del_glacier.append((i,j))

    # delete set of glacier_positions in order to reduce time_complexity
    glacier = list(set(glacier) - set(del_glacier))
    
    num_years += 1
        


# import sys
# from collections import deque
# input = sys.stdin.readline

# # input
# x, y = map(int, input().split(' '))
# glacier = []
# for _ in range(x):
#     glacier.append(list(map(int, input().split(' '))))
# ice = []

# for i in range(x):
#     for j in range(y):
#         if glacier[i][j] != 0:
#             ice.append((i,j))    

# def bfs(i, j, visited, to_visit):
#     to_visit.append((i,j))
#     visited[i][j] = True
#     while to_visit:
#         cur_visit = to_visit.popleft()
#         for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
#             next_visit = (cur_visit[0] + dx, cur_visit[1] + dy)
#             if 0 <= next_visit[0] < x and 0 <= next_visit[1] < y:
#                 if glacier[next_visit[0]][next_visit[1]] > 0 and visited[next_visit[0]][next_visit[1]] == False:
#                     to_visit.append(next_visit)
#                     visited[next_visit[0]][next_visit[1]] = True

# def find_melt(i,j):
#     cnt = 0
#     for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
#         adj = (i + dx, j + dy)
#         if 0 <= adj[0] < x and 0 <= adj[1] < y:
#             if glacier[adj[0]][adj[1]] <= 0:
#                 cnt += 1
#     return ((i,j), cnt)

# #

# num_years = 0

# while True:
#     visited = [[False for _ in range(y)] for _ in range(x)]
#     to_visit = deque()
#     cnt = 0
#     to_melt = []
#     all_melted = True
#     del_ice = []
#     # BFS : 빙산 갯수 찾기
#     for (i,j) in ice:
#     # for i in range(x):
#         # for j in range(y):
#             # 다음 해에 얼마나 녹을지 찾기
#             # [((i,j), n), ...]
#             to_melt.append(find_melt(i,j))
#             # 분리된 빙산 찾기 위한 BFS
#             if glacier[i][j] > 0 and visited[i][j] == False:
#                 all_melted = False
#                 cnt += 1
#                 bfs(i, j, visited, to_visit)
#     # 빙산이 없으면 중단
#     if all_melted:
#         print(0)
#         break
#     # 빙산이 분리되면 중단
#     if cnt > 1:
#         print(num_years)
#         break
#     # 해 증가
#     num_years += 1
#     # 빙산 녹이기
#     for ((i,j), n) in to_melt:
#         glacier[i][j] -= n
#         if glacier[i][j] <= 0:
#             del_ice.append((i,j))
#     ice = list(set(ice)-set(del_ice))