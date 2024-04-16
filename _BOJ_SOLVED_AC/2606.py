########################################
# DFS - 재귀, Graph 를 dict 로 구현

# import sys
# input = sys.stdin.readline

# num_v = int(input())
# num_e = int(input())
# graph = {v:[] for v in range(1, num_v + 1)}
# for _ in range(num_e):
#     from_v, to_v = map(int, input().split(' '))
#     graph[from_v].append(to_v)
#     graph[to_v].append(from_v)

# visited = [False] * (num_v + 1)

# def dfs(start_v):
#     visited[start_v] = True
#     for i in graph[start_v]:
#         if visited[i] == False:
#             dfs(i)

# dfs(1)

# cnt = 0
# for i in range(1, num_v+1):
#     if visited[i]:
#         cnt += 1

# print(cnt-1)


########################################
# DFS - Graph 를 리스트로 구현

# import sys
# input = sys.stdin.readline

# num_v = int(input())
# num_e = int(input())
# graph = [[] for i in range(0, num_v+1)]

# for _ in range(num_e):
#     from_v, to_v = map(int, input().split(' '))
#     graph[from_v].append(to_v)
#     graph[to_v].append(from_v)

# visited = [False] * (num_v + 1)

# def dfs(start_v):
#     visited[start_v] = True
#     for i in graph[start_v]:
#         if visited[i] == False:
#             dfs(i)

# dfs(1)

# cnt = 0
# for i in range(1, num_v+1):
#     if visited[i]:
#         cnt += 1

# print(cnt-1)

# ########################################
# # DFS - Deque 를 이용한 반복문으로 구현

# import sys
# from collections import deque
# input = sys.stdin.readline

# num_v = int(input())
# num_e = int(input())
# graph = {v:[] for v in range(1, num_v + 1)}
# for _ in range(num_e):
#     from_v, to_v = map(int, input().split(' '))
#     graph[from_v].append(to_v)
#     graph[to_v].append(from_v)

# visited = [False for _ in range(num_v+1)]
# to_visit = deque()

# # visited[1] = True
# to_visit.append(1)

# while to_visit:
#     cur_v = to_visit.pop()
#     if visited[cur_v] == True:
#         continue
#     else:
#         visited[cur_v] = True
#         to_visit.extend(graph[cur_v])

# cnt = 0
# for i in range(1, num_v+1):
#     if visited[i]:
#         cnt += 1

# print(cnt-1)

########################################
# BFS - Deque 를 이용한 반복문으로 구현

import sys
from collections import deque
input = sys.stdin.readline

num_v = int(input())
num_e = int(input())
graph = {v:[] for v in range(1, num_v + 1)}
for _ in range(num_e):
    from_v, to_v = map(int, input().split(' '))
    graph[from_v].append(to_v)
    graph[to_v].append(from_v)

visited = [False for _ in range(num_v+1)]
to_visit = deque()

# visited[1] = True
to_visit.append(1)

while to_visit:
    cur_v = to_visit.popleft()
    if visited[cur_v] == True:
        continue
    else:
        visited[cur_v] = True
        to_visit.extend(graph[cur_v])

cnt = 0
for i in range(1, num_v+1):
    if visited[i]:
        cnt += 1

print(cnt-1)