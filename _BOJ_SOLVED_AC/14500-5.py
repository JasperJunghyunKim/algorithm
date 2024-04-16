import sys
sys_input = sys.stdin.readline

NUM_ROW, NUM_COL = map(int, sys_input().split())
number_map = [list(map(int, sys_input().split())) for _ in range(NUM_ROW)]

visited = [(-1, -1)] * 4
len_visited = 0
cur_max = 0
def recursive(cur_row, cur_col):
    global len_visited
    global cur_max

    if len_visited == 4:
        tmp_max = 0
        for r, c in visited:
            tmp_max += number_map[r][c]
        cur_max = tmp_max if tmp_max > cur_max else cur_max
        return
    
    for d_r, d_c in [(0,1), (0,-1), (1,0), (-1,0)]:
        next_row, next_col = cur_row + d_r, cur_col + d_c
        if (next_row, next_col) not in visited and 0 <= next_row < NUM_ROW and 0 <= next_col < NUM_COL:
            visited[len_visited] = (next_row, next_col)
            len_visited += 1
            recursive(next_row, next_col)
            len_visited -= 1
            visited[len_visited] = (-1, -1)

# All Tetrominos except ㅓ,ㅏ,ㅗ,ㅜ
for cur_row in range(NUM_ROW):
    for cur_col in range(NUM_COL):
        visited[len_visited] = (cur_row, cur_col)
        len_visited += 1
        recursive(cur_row, cur_col)
        len_visited -= 1
        visited[len_visited] = (-1, -1)
        
        # ㅏ ㅓ
        if cur_row < NUM_ROW - 2 and cur_col < NUM_COL - 1:
            # ㅏ : [(0,0), (1,0), (2,0), (1,1)]
            tmp_max = 0
            for d_r, d_c in [(0,0), (1,0), (2,0), (1,1)]:
                next_row, next_col = cur_row + d_r, cur_col + d_c
                tmp_max +=  number_map[next_row][next_col]
            cur_max = tmp_max if tmp_max > cur_max else cur_max
            # ㅓ : [(1,0), (0,1), (1,1), (2,1)] 
            tmp_max = 0
            for d_r, d_c in [(1,0), (0,1), (1,1), (2,1)]:
                next_row, next_col = cur_row + d_r, cur_col + d_c
                tmp_max +=  number_map[next_row][next_col]
            cur_max = tmp_max if tmp_max > cur_max else cur_max
            
        # ㅗ ㅜ
        if cur_row < NUM_ROW - 1 and cur_col < NUM_COL - 2:
            # ㅗ : [(0,1), (1,0), (1,1), (1,2)]
            tmp_max = 0
            for d_r, d_c in [(0,1), (1,0), (1,1), (1,2)]:
                next_row, next_col = cur_row + d_r, cur_col + d_c
                tmp_max +=  number_map[next_row][next_col]
            cur_max = tmp_max if tmp_max > cur_max else cur_max
            # ㅜ : [(0,0), (0,1), (0,2), (1,1)]
            tmp_max = 0
            for d_r, d_c in [(0,0), (0,1), (0,2), (1,1)]:
                next_row, next_col = cur_row + d_r, cur_col + d_c
                tmp_max +=  number_map[next_row][next_col]
            cur_max = tmp_max if tmp_max > cur_max else cur_max
        
print(cur_max)