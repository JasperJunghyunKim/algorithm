#
# 24-03-11
# DFS - recursive, stack
# BFS - queue(deque)
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
dfs_visited_rec = []

def dfs(cur_v):
    dfs_visited_rec.append(cur_v)
    for next_v in range(1, num_v + 1):
        if graph[cur_v][next_v] == 1 and next_v not in dfs_visited_rec:
            dfs(next_v)

dfs(start_v)
print(*dfs_visited_rec)


# DFS - stack
# BFS queue 와 동일하게 코드를 작성하면 문제 조건의 순회 순서를 지키지 못함
# 따라서 다음 조건을 추가하여 해결함
# 1. to_visit pop 된 다음에 visited 에 추가
# 2. to_visit append 하기 전에, next_v 가 이미 to_visit 에 있다면 remove

dfs_visited_stk = []
to_visit = []
to_visit.append(start_v)

while to_visit:
    cur_v = to_visit.pop()
    dfs_visited_stk.append(cur_v)
    for next_v in range(num_v, 0, -1):
        if graph[cur_v][next_v] == 1 and next_v not in dfs_visited_stk:
            if next_v in to_visit:
                to_visit.remove(next_v)
            to_visit.append(next_v)

print(*dfs_visited_stk)

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
