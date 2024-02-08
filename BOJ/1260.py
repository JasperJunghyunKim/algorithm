########################################
# 23-12-14
# [중요] BFS 는 deque(queue) 를 이용, DFS 는 recursive 또는 stack 을 이용하는 것으로 알고있었다. 
# 그러나 DFS stack 을 이용할 경우 순회는 모두 되지만, 순서가 지켜지지 않는 오류가 있음을 발견함. → 아래 dfs recursive 코드 참조
import sys
from collections import deque
sys_input = sys.stdin.readline

num_vertex, num_edge, start = map(int, sys_input().split())
graph = [[0 for _ in range(num_vertex + 1)] for _ in range(num_vertex + 1)]
for _ in range(num_edge):
    a, b = map(int, sys_input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# dfs - recursive
dfs_visited1 = []
def dfs(cur_v):
    dfs_visited1.append(cur_v)
    for next_v in range(1, num_vertex+1):
        if graph[cur_v][next_v] == 1 and next_v not in dfs_visited1:
            dfs(next_v)
dfs(start)
print(*dfs_visited1)

# [순서 오류] dfs - stack(deque) (1)
# 방문 순서가 지켜지지 않음 → 단순히 deque 을 queue 에서 stack 으로 사용한다고 dfs 가 되는 게 아니었음
dfs_visited2 = []
dfs_visited2.append(start)
to_visit = deque()
to_visit.append(start)
while(to_visit):
    cur_v = to_visit.pop()
    for next_v in reversed(range(1, num_vertex + 1)):
        if graph[cur_v][next_v] == 1 and next_v not in dfs_visited2:
            dfs_visited2.append(next_v)
            to_visit.append(next_v)
print(*dfs_visited2)

# dfs - stack(deque) (2)
dfs_visited3 = []
to_visit = deque()
to_visit.append(start)
while to_visit:
    cur_v = to_visit.pop()
    if cur_v in dfs_visited3: continue
    dfs_visited3.append(cur_v)
    for next_v in reversed(range(1, num_vertex + 1)):
        if graph[cur_v][next_v] == 1 and next_v not in dfs_visited3:
            to_visit.append(next_v)
print(*dfs_visited3)

# bfs - queue(deque)
bfs_visited = []
bfs_visited.append(start)
to_visit = deque()
to_visit.append(start)
while(to_visit):
    cur_v = to_visit.popleft()
    for next_v in range(1, num_vertex + 1):
        if graph[cur_v][next_v] == 1 and next_v not in bfs_visited:
            bfs_visited.append(next_v)
            to_visit.append(next_v)
print(*bfs_visited)