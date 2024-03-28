#
# 24-03-21
# 
import sys
from collections import deque
NUM_V, NUM_E, START_V = map(int, sys.stdin.readline().split(' '))
adj_maxtrix = [[False for _ in range(NUM_V + 1)] for _ in range(NUM_V + 1)]
adj_list = {i:[] for i in range(1, NUM_V + 1)}
for _ in range(NUM_E):
    v1, v2 = map(int, sys.stdin.readline().split(' '))
    
    adj_maxtrix[v1][v2] = True
    adj_maxtrix[v2][v1] = True
    
    adj_list[v1].append(v2)
    adj_list[v2].append(v1)
    
    
# DFS - Recursive
dfs_visited = []
def dfs(cur_v):
    dfs_visited.append(cur_v)
    for next_v in range(1, NUM_V + 1):
        if adj_maxtrix[cur_v][next_v] == True and next_v not in dfs_visited:
            dfs(next_v)
            
dfs(START_V)
print(*dfs_visited, sep=" ")

    
# BFS - Queue - ADJ MATRIX
bfs_visited = [START_V]
bfs_to_visit = deque([START_V])
while bfs_to_visit:
    cur_v = bfs_to_visit.popleft()
    for next_v in range(1, NUM_V + 1):
        if adj_maxtrix[cur_v][next_v] == True and next_v not in bfs_visited:
            bfs_visited.append(next_v)
            bfs_to_visit.append(next_v)
    
print(*bfs_visited, sep=" ")

# BFS - Queue - ADJ LIST
bfs_visited = [START_V]
bfs_to_visit = deque([START_V])
for k in adj_list.keys():
    adj_list[k].sort()
    
while bfs_to_visit:
    cur_v = bfs_to_visit.popleft()
    for next_v in adj_list[cur_v]:
        if next_v not in bfs_visited:
            bfs_visited.append(next_v)
            bfs_to_visit.append(next_v)
    
print(*bfs_visited, sep=" ")

