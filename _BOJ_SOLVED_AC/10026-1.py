import sys
sys_input = sys.stdin.readline
from collections import deque

N = int(sys_input().strip())
color_map = [list(sys_input().strip()) for _ in range(N)]

def get_num_sectors(is_color_blind):
    visited = [[False] * N for _ in range(N)]
    num_sectors = 0
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                num_sectors += 1
                visited[r][c] = True
                to_visit = deque([(r,c)])
                while to_visit:
                    cur_r, cur_c = to_visit.popleft()
                    for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                        next_r, next_c = cur_r + dr, cur_c + dc
                        # 격자 내, 미방문
                        if 0 <= next_r < N and 0 <= next_c < N:
                            if not visited[next_r][next_c]:
                                if is_color_blind:
                                    if color_map[cur_r][cur_c] == "R" or color_map[cur_r][cur_c] == "G":
                                        if color_map[next_r][next_c] == "R" or color_map[next_r][next_c] == "G":
                                            visited[next_r][next_c] = True
                                            to_visit.append((next_r, next_c))
                                    if color_map[cur_r][cur_c] == "B" and color_map[next_r][next_c] == "B":
                                        visited[next_r][next_c] = True
                                        to_visit.append((next_r, next_c))
                                else:
                                    if color_map[cur_r][cur_c] == color_map[next_r][next_c]:
                                        visited[next_r][next_c] = True
                                        to_visit.append((next_r, next_c))
    return num_sectors

print(get_num_sectors(is_color_blind = False), get_num_sectors(is_color_blind = True))