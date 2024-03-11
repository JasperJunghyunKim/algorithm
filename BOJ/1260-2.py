#
# 24-03-11
# DFS - 
# BFS
# 

import sys
from collections import deque
sys_input = sys.stdin.readline

num_v, num_e, start_v = map(int, sys_input().split())

graph = [[0 for _ in range(num_v + 1)] for _ in range(num_v + 1)]
for _ in range(num_e):
    a, b = map(int, sys_input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# DFS - recursive
dfs_visited1 = []
def dfs(cur_v):
    dfs_visited1.append(cur_v)
    for next_v in range(1, num_v + 1):
        if graph[cur_v][next_v] == 1 and next_v not in dfs_visited1:
            dfs(next_v)

dfs(start_v)
print(*dfs_visited1)

# DFS - stack

# BFS - queue(deque)
bfs_visited = []
bfs_visited.append(start_v)
to_visit = deque()
to_visit.append(start_v)
while(to_visit):
    cur_v = to_visit.popleft()
    for next_v in range(1, num_v + 1):
        if graph[cur_v][next_v] == 1 and next_v not in bfs_visited:
            bfs_visited.append(next_v)
            to_visit.append(next_v)
print(*bfs_visited)
