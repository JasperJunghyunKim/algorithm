#
# 24-03-21
# 
import sys
from collections import deque
NUM_V, NUM_E, START_V = map(int, sys.stdin.readline().split(' '))
graph = [[False for _ in range(NUM_V + 1)] for _ in range(NUM_V + 1)]
for _ in range(NUM_E):
    v1, v2 = map(int, sys.stdin.readline().split(' '))
    graph[v1][v2] = True
    graph[v2][v1] = True

# DFS
dfs_visited = []

def dfs(cur_v):
    for next_v in range(1, NUM_V + 1):
        if graph[cur_v][next_v] == True and next_v not in dfs_visited:
            dfs_visited.append(next_v)
            dfs(next_v)
            
dfs_visited.append(START_V)
dfs(START_V)   
print(*dfs_visited)    

# BFS
bfs_visited = [START_V]
bfs_to_visit = deque([START_V])

while bfs_to_visit:
    cur_v = bfs_to_visit.popleft()
    for next_v in range(1, NUM_V + 1):
        if graph[cur_v][next_v] == True and next_v not in bfs_visited:
            bfs_visited.append(next_v)
            bfs_to_visit.append(next_v)

print(*bfs_visited)