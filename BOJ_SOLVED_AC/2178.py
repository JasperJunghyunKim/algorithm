########################################
# T2 - BFS 
########################################
import sys
from collections import deque
input = sys.stdin.readline

row, col = map(int, input().split(' '))
graph = []
to_visit = []

for _ in range(row):
    graph.append(list(input().strip()))

# MAIN
to_visit.append((0,0))
graph[0][0] = -1
while to_visit:
    next_visit = []
    for cur_row, cur_col in to_visit:
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            next_row, next_col = cur_row + dr, cur_col + dc
            if 0 <= next_row < row and 0 <= next_col < col:
                if graph[next_row][next_col] == '1':
                    next_visit.append((next_row, next_col))
                    graph[next_row][next_col] = graph[cur_row][cur_col] - 1
    to_visit = next_visit

print(abs(graph[row-1][col-1]))

########################################
# T1 - DFS Recursive
########################################

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**4)
# row, col = map(int, input().split(' '))
# graph = []
# visited = [[-1 for _ in range(col)] for _ in range(row)]

# for _ in range(row):
#     graph.append(list(input().strip()))

# def dfs(cur_row, cur_col, cur_cnt):
#     visited[cur_row][cur_col] = cur_cnt
#     for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
#         next_row, next_col = cur_row + dr, cur_col + dc
#         # 범위 내
#         # 이동 가능
#         # 방문 전 또는 현 방문 cnt 가 더 작음
#         if 0 <= next_row < row and 0 <= next_col < col:
#             if graph[next_row][next_col] == '1':
#                 if visited[next_row][next_col] == -1 or visited[next_row][next_col] > cur_cnt + 1:
#                     dfs(next_row, next_col, cur_cnt+1)

# # MAIN
# dfs(0, 0, 1)
# print(visited[row-1][col-1])