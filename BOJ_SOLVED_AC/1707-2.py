from collections import deque
import sys
sys_input = sys.stdin.readline
sys.setrecursionlimit(200_010)
NUM_TC = int(sys_input().strip())

def dfs(cur_v):
    global is_bipartite
    if not is_bipartite: return
    for next_v in graph[cur_v]:
        if visited[next_v] == 0:
            visited[next_v] = (-visited[cur_v])
            dfs(next_v)
        elif visited[next_v] == visited[cur_v]:
            is_bipartite = False

for _ in range(NUM_TC):
    NUM_V, NUM_E = map(int, sys_input().strip().split())
    graph = {i:[] for i in range(1, NUM_V + 1)}
    for _ in range(NUM_E):
        a, b = map(int, sys_input().strip().split())
        graph[a].append(b)
        graph[b].append(a)
        
    is_bipartite = True
    visited = [0 for _ in range(NUM_V + 1)]
    
    for v in range(1, NUM_V + 1):
        if not is_bipartite: break
        if not visited[v]:
            visited[v] = 1
            # DFS 실행하거나
            dfs(v)
            
            # BFS 실행하는 방법도 있음
            # 코드는 지워버림
    if not is_bipartite: 
        print("NO")
    else:
        print("YES")