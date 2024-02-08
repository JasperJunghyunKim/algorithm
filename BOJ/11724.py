import sys
sys_input = sys.stdin.readline

num_vertex, num_edge = map(int, sys_input().split(' '))
parent = [i for i in range(0, num_vertex + 1)]
root = [i for i in range(0, num_vertex + 1)]


def find_root(x):
    if parent[x] == x: return x
    parent[x] = find_root(parent[x])
    return parent[x]

def union(x,y):
    x = find_root(x)
    y = find_root(y)
    if x == y: return
    elif x < y: parent[y] = x
    return

for _ in range(num_edge):
    vertex_a, vertex_b = map(int, sys_input().split(' '))
    union(vertex_a, vertex_b)

for i in range(num_vertex + 1):
    root[i] = find_root(i) # 모든 vertex 에 대해 부모를 root 로 바꿔줘야 함
root = set(root[1:])
print(len(root))

########################################
# T1: BFS, DFS
########################################
# import sys
# sys_input = sys.stdin.readline
# sys.setrecursionlimit(1000**2)
# from collections import deque

# num_vertex, num_edge = map(int, sys_input().split(' '))
# connection = [[False for _ in range(num_vertex + 1)] for _ in range(num_vertex + 1)]
# visited = [False for _ in range(num_vertex + 1)]
# for _ in range(num_edge):
#     vertex_a, vertex_b = map(int, sys_input().split(' '))
#     connection[vertex_a][vertex_b] = True
#     connection[vertex_b][vertex_a] = True

# def dfs_recursive(cur_vertex):
#     visited[cur_vertex] = True
#     for next_vertex in range(1, num_vertex + 1):
#         if connection[cur_vertex][next_vertex] == True:
#             if visited[next_vertex] == False:
#                 dfs(next_vertex)

# def bfs(vertex):
#     visited[vertex] = True
#     next_visit = deque()
#     next_visit.append(vertex)
#     while next_visit:
#         cur_vertex = next_visit.popleft()
#         for next_vertex in range(1, num_vertex + 1):
#             if connection[cur_vertex][next_vertex] == True:
#                 if visited[next_vertex] == False:
#                     visited[next_vertex] = True
#                     next_visit.append(next_vertex)

# def dfs(vertex):
#     visited[vertex] = True
#     next_visit = deque()
#     next_visit.append(vertex)
#     while next_visit:
#         cur_vertex = next_visit.pop()
#         for next_vertex in range(1, num_vertex + 1):
#             if connection[cur_vertex][next_vertex] == True:
#                 if visited[next_vertex] == False:
#                     visited[next_vertex] = True
#                     next_visit.append(next_vertex)

# cnt = 0
# for vertex in range(1, num_vertex + 1):
#     if visited[vertex] == False:
#         cnt += 1
#         # dfs_recursive(vertex)
#         dfs(vertex)
#         # bfs(vertex)
# print(cnt)