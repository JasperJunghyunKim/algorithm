import sys
sys_input = sys.stdin.readline
from collections import deque

while True:
    W, H = map(int, sys_input().strip().split())
    if W == 0 and H == 0: break

    num_islands = 0
    graph = [list(map(int, sys_input().strip().split())) for _ in range(H)]
    visited = [[False] * W for _ in range(H)]

    for r in range(H):
        for c in range(W):
            if not visited[r][c] and graph[r][c] == 1:
                num_islands += 1
                visited[r][c] = True
                to_visit = deque([(r,c)])
                while to_visit:
                    cur_r, cur_c = to_visit.popleft()
                    for dr, dc in [(0,1), (1,0), (-1,0), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1)]:
                        next_r, next_c = cur_r + dr, cur_c + dc
                        # 격자 범위 내에서
                        # 인접한 방문하지 않은 땅일때
                        if 0 <= next_r < H and 0 <= next_c < W:
                            if not visited[next_r][next_c] and graph[next_r][next_c] == 1:
                                visited[next_r][next_c] = True
                                to_visit.append((next_r, next_c))
    print(num_islands)