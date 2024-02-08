from collections import deque

def solution(maps):
    answer = 0
    width = len(maps[0])
    height = len(maps)
    visited = [[(False, 0) for _ in range(width)] for _ in range(height)]

    visited[0][0] = (True, 1)
    to_visit = deque()
    to_visit.append((0,0))
    while to_visit:
        cur_row, cur_col = to_visit.popleft()
        cur_cnt = visited[cur_row][cur_col][1]
        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            next_row, next_col = cur_row + dr, cur_col + dc
            # in range
            # valid movement
            # not visited or lower count value
            if 0 <= next_row < height and 0 <= next_col < width:
                if maps[next_row][next_col] == 1:
                    if visited[next_row][next_col][0] == False or visited[next_row][next_col][1] > cur_cnt + 1:
                        visited[next_row][next_col] = (True, cur_cnt + 1)
                        to_visit.append((next_row, next_col))
    
    if visited[height-1][width-1][0] == False: answer = -1
    else : answer = visited[height-1][width-1][1]
    return answer

