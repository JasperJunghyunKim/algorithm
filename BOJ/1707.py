import sys
sys_input = sys.stdin.readline
from collections import deque

BLUE = 0
RED = 1

def bfs(val):
    next_visit = deque()
    visited[val] = BLUE
    next_visit.append(val)
    while next_visit:
        cur_val = next_visit.popleft()
        for next_val in graph[cur_val]:
            # if not visited, color next color
            if visited[next_val] == -1:
                if visited[cur_val] == BLUE: visited[next_val] = RED
                elif visited[cur_val] == RED: visited[next_val] = BLUE
                next_visit.append(next_val)
            elif visited[next_val] != -1 and visited[cur_val] == visited[next_val]:
                return False
    return True     

tc = int(sys_input())
for _ in range(tc):
    num_v, num_e = map(int, sys_input().split(' '))
    graph = {i:[] for i in range(1, num_v+1)}
    visited = [-1 for _ in range(num_v + 1)]
    for _ in range(num_e):
        vertex_a, vertex_b = map(int, sys_input().split(' '))
        graph[vertex_a].append(vertex_b)
        graph[vertex_b].append(vertex_a)
    is_bipartite = True
    for i in range(1, num_v + 1):
        if visited[i] == -1:
            is_bipartite = is_bipartite and bfs(i)
    if is_bipartite:
        print('YES')
    else:
        print('NO')