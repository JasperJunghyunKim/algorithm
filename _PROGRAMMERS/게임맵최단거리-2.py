#
# 24-03-18
# DFS Stack 시간초과 -> BFS Queue 로만 바꿨더니 통과
#
from collections import deque

def solution(maps):
    num_row = len(maps)
    num_col = len(maps[0])
    
    # to_visit = []
    to_visit = deque()
    visited = [[-1 for _ in range(num_col)] for _ in range(num_row)]
    to_visit.append((0,0))
    visited[0][0] = 1
    
    while to_visit:
        # cur_r, cur_c = to_visit.pop()
        cur_r, cur_c = to_visit.popleft()
        for d_r, d_c in [(1,0), (-1,0), (0,1), (0,-1)]:
            next_r, next_c = cur_r + d_r, cur_c + d_c
            if 0 <= next_r < num_row and 0 <= next_c < num_col:
                if maps[next_r][next_c] == 1 and (visited[next_r][next_c] == -1 or visited[next_r][next_c] > visited[cur_r][cur_c] + 1):
                    to_visit.append((next_r, next_c))
                    visited[next_r][next_c] = visited[cur_r][cur_c] + 1
    
    return visited[num_row - 1][num_col - 1]
