import sys
sys_input = sys.stdin.readline
N = int(sys_input().strip())
graph = [list(map(int, sys_input().strip().split())) for _ in range(N)]
for r in range(N):
    for c in range(N):
        if graph[r][c] == 0: graph[r][c] = float('inf')

for step_over in range(N):
    for a in range(N):
        for b in range(N):
            graph[a][b] = min(graph[a][b], graph[a][step_over] + graph[step_over][b])

for r in range(N):
    for c in range(N):
        if graph[r][c] == float('inf'): graph[r][c] = 0
        else: graph[r][c] = 1

for x in graph:
    print(*x)