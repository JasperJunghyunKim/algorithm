import sys
sys_input = sys.stdin.readline
from collections import deque

for _ in range(int(sys_input().strip())):
    N = int(sys_input().strip())
    start_r, start_c = map(int, sys_input().strip().split())
    end_r, end_c = map(int, sys_input().strip().split())
    if start_r == end_r and start_c == end_c:
        print(0)
        continue
    end_point_found = False
    cnts_to_end_point = 0
    visited = [[False] * N for _ in range(N)]
    visited[start_r][start_c] = True
    to_visit = deque([(start_r, start_c, 0)])
    while to_visit:
        if end_point_found: break
        cur_r, cur_c, cur_cnt = to_visit.popleft()
        for dr, dc in [(1, -2), (2,-1), (1,2),(2,1), (-1,-2), (-2,-1),(-1,2), (-2,1)]:
            next_r, next_c = cur_r + dr, cur_c + dc
            if next_r == end_r and next_c == end_c:
                end_point_found = True
                cnts_to_end_point = cur_cnt + 1
                break
            if 0 <= next_r < N and 0 <= next_c < N:
                if not visited[next_r][next_c]:
                    visited[next_r][next_c] = True
                    to_visit.append((next_r, next_c, cur_cnt + 1))
    print(cnts_to_end_point)