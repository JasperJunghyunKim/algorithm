#
# 실패
#

from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    num_rectangle = len(rectangle)
    
    # draw game map
    # 직사각형마다 다른 숫자 부여
    game_map = [[0 for _ in range(51)] for _ in range(51)]
    for index, (x1, y1, x2, y2) in enumerate(rectangle):
        for x in range(x1, x2 + 1):
            game_map[x][y1] = index + 1
            game_map[x][y2] = index + 1
        for y in range(y1, y2 + 1):
            game_map[x1][y] = index + 1
            game_map[x2][y] = index + 1

    # dfs
    visited = [[False for _ in range(51)] for _ in range(51)]
    visited[characterX][characterY] = True
    to_visit = deque()    
    to_visit.append((characterX, characterY, 0))
    while to_visit:
        cur_x, cur_y, cur_cnt = to_visit.pop()
        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            next_x, next_y = cur_x + dx, cur_y + dy
            # in range
            # not visited
            # 
            if 1 <= next_x <= 50 and 1 <= next_y <= 50:
                


    return answer