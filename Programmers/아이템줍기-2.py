#
# 24-03-18
# BFS
# 시작점에서 -> ITEM 까지 BFS 로 탐색하는데, 직사각형의 변을 따라서, + 다른 직사각형에 포함이 안되었는지를 조건으로 탐색
# (중요) 그리고 ㄷ 자 부분에서 ㄷ 모양대로 이동하지 않고, 인접한 것으로 인지하여 점프하게 되는데, 이 것을 방지하기 위해 map 사이즈를 2 배로 키움
#

from collections import deque

is_visited = [[-1 for _ in range(101)] for _ in range(101)]
to_visit = deque()

def is_overlap(row, col, rectangle):
    for row_min, col_min, row_max, col_max in rectangle:
        if row_min + 1 <= row <= row_max - 1 and col_min + 1 <= col <= col_max -1:
            return True
    else: 
        return False
                
def is_edge(row, col, rectangle):
    for row_min, col_min, row_max, col_max in rectangle:
        if row_min <= row <= row_max and (col == col_min or col == col_max):
            return True
        elif col_min <= col <= col_max and (row == row_min or row == row_max):
            return True

    else: 
        return False
    
def same_rectangle(cur_row, cur_col, next_row, next_col, rectangle):
    cur_rec = []
    next_rec = []
    for rec_no, (row_min, col_min, row_max, col_max) in enumerate(rectangle):
        if row_min <= cur_row <= row_max and col_min <= cur_col <= col_max:
            cur_rec.append(rec_no)
        if row_min <= next_row <= row_max and col_min <= next_col <= col_max:
            next_rec.append(rec_no)
    for i in cur_rec:
        for j in next_rec:
            if i == j: return True
    return False

def solution(rectangle, characterX, characterY, itemX, itemY):
    
    double_rectangle = []
    for r1, r2, r3, r4 in rectangle:
        double_rectangle.append([r1 * 2, r2 * 2, r3 * 2, r4 * 2])
    
    is_visited[characterX * 2][characterY * 2] = 0
    to_visit.append((characterX * 2, characterY * 2))
    while to_visit:
        cur_row, cur_col = to_visit.popleft()
        for d_r, d_c in [(0,1), (0,-1), (1,0), (-1,0)]:
            next_row, next_col = cur_row + d_r, cur_col + d_c
            if 1 <= next_row <= 100 and 1 <= next_col <= 100:
                if is_edge(next_row, next_col, double_rectangle):
                    if not is_overlap(next_row, next_col, double_rectangle):
                        if is_visited[next_row][next_col] == -1:
                            # if not same_rectangle(cur_row, cur_col, next_row, next_col, rectangle): continue
                            is_visited[next_row][next_col] = is_visited[cur_row][cur_col] + 1
                            to_visit.append((next_row, next_col))
    
    return is_visited[itemX][itemY] // 2