game_board = [[0,0,0],[1,1,0],[1,1,1]]	
table = [[1,1,1],[1,0,0],[0,0,0]]	

from collections import deque
SIZE = None
visited = None


# return blank path, blank height, blank width
def find_blank(game_board, r,c):
    if visited[r][c]:
        return [], 0, 0
    # BFS 시작
    min_r, min_c = 100, 100
    max_r, max_c = -100, -100
    visited[r][c] = True
    to_visit = deque([(r,c)])
    visited_path = [(r,c)]
    min_r = r if r < min_r else min_r
    min_c = c if c < min_c else min_c
    max_r = r if r > max_r else max_r
    max_c = c if c > max_c else max_c
    while to_visit:
        cur_r, cur_c = to_visit.popleft()
        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            next_r, next_c = cur_r + dr, cur_c + dc
            # 격자 내, 미방문, 빈칸
            if 0 <= next_r < SIZE and 0 <= next_c < SIZE:
                if game_board[next_r][next_c] == 0 and not visited[next_r][next_c]:
                    visited[next_r][next_c] = True
                    to_visit.append((next_r, next_c))
                    visited_path.append((next_r, next_c))
                    min_r = next_r if next_r < min_r else min_r
                    min_c = next_c if next_c < min_c else min_c
                    max_r = next_r if next_r > max_r else max_r
                    max_c = next_c if next_c > max_c else max_c
    # BFS 종료
    # min_r, min_c 기준으로 상대적 위치를 구함
    deg_0_height = max_r - min_r + 1
    deg_0_width = max_c - min_c + 1
    deg_0_blank_map = [[0] * deg_0_width for _ in range(deg_0_height)]
    for r, c in visited_path:
        deg_0_blank_map[r - min_r][c - min_c] = 1
    # print(*deg_0_blank_map, sep="\n")

    # 90
    deg_90_height = deg_0_width
    deg_90_width = deg_0_height
    deg_90_blank_map = [[0] * deg_90_width for _ in range(deg_90_height)]

    for r in range(deg_0_height):
        for c in range(deg_0_width):
            deg_90_blank_map[c][deg_90_width - r - 1] = deg_0_blank_map[r][c]
    # print(*deg_90_blank_map, sep="\n")
    
    # # 180
    deg_180_height = deg_0_height
    deg_180_width = deg_0_width
    deg_180_blank_map = [[0] * deg_180_width for _ in range(deg_180_height)]
    for r in range(deg_0_height):
        for c in range(deg_0_width):
            deg_180_blank_map[deg_180_height - r - 1][deg_180_width - c - 1] = deg_0_blank_map[r][c]
    # print(*deg_180_blank_map, sep="\n")
    
    # # 270
    deg_270_height = deg_0_width
    deg_270_width = deg_0_height
    deg_270_blank_map = [[0] * deg_270_width for _ in range(deg_270_height)]
    for r in range(deg_0_height):
        for c in range(deg_0_width):
            deg_270_blank_map[deg_270_height - c - 1][r] = deg_0_blank_map[r][c]
    # print(*deg_270_blank_map, sep="\n")
            
    return [deg_0_blank_map, deg_90_blank_map, deg_180_blank_map, deg_270_blank_map], [deg_0_height, deg_90_height, deg_180_height, deg_270_height], [deg_0_width, deg_90_width, deg_180_width, deg_270_width]
    

def solution(game_board, table):
    global SIZE
    global visited
    SIZE = len(game_board)
    visited = [[False] * SIZE for _ in range(SIZE)]
    num_filled = 0
    
    
    for r in range(SIZE):
        for c in range(SIZE):
            blank_map_list, blank_height_list, blank_width_list = find_blank(game_board, r, c)    
            if not blank_map_list: continue
            # 각 회전 모양에 대하여
            is_match = False
            for i in range(4):
                if is_match:
                    break

                blank_map = blank_map_list[i]
                blank_height = blank_height_list[i]
                blank_width = blank_width_list[i]
                print(blank_map, blank_height, blank_width)
                for table_r in range(SIZE - blank_height + 1):
                    if is_match:
                        break   
                    for table_c in range(SIZE - blank_width + 1):
                        if is_match:
                            break
                        # 
                        is_same = True
                        for dr in range(blank_height):
                            if is_match:
                                break
                            for dc in range(blank_width):
                                if blank_map[dr][dc] == 1 and table[table_r + dr][table_c + dc] == 0:
                                    is_same = False
                                    break
                            if not is_same:
                                break
                        # 
                        if is_same:
                            is_match = True
                            for dr in range(blank_height):
                                for dc in range(blank_width):
                                    if blank_map[dr][dc] == 1:
                                        table[table_r + dr][table_c + dc] = 0
                                        num_filled += 1
                            
                                
    
    
    
    return num_filled
    
print(solution(game_board, table))