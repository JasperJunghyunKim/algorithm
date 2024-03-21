import sys
sys_input = sys.stdin.readline

NUM_ROW, NUM_COL = map(int, sys_input().split(' '))
number_map = [list(map(int, sys_input().split(' '))) for _ in range(NUM_ROW)]
max_value = [0]
visited = [[False for _ in range(NUM_COL)] for _ in range(NUM_ROW)]

def recursive(cur_r, cur_c, cur_depth, cur_total):
    
    if cur_depth == 4:
        max_value[0] = cur_total if cur_total > max_value[0] else max_value[0]
        return
    
    for d_r, d_c in [(0,1), (0,-1), (1,0), (-1,0)]:
        next_r, next_c = cur_r + d_r, cur_c + d_c
        if 0 <= next_r < NUM_ROW and 0 <= next_c < NUM_COL and visited[next_r][next_c] == False:
            if cur_depth == 2:
                visited[next_r][next_c] = True
                recursive(cur_r, cur_c, cur_depth + 1, cur_total + number_map[next_r][next_c])
                visited[next_r][next_c] = False
            visited[next_r][next_c] = True
            recursive(next_r, next_c, cur_depth + 1, cur_total + number_map[next_r][next_c])
            visited[next_r][next_c] = False

    return
# ㅗ ㅜ
updown = [[(0,0), (0,1), (0,2), (1,1)],[(1,0), (1,1), (1,2), (0,1)]]
# ㅓ ㅏ
rightleft = [[(0,0), (1,0), (2,0), (1,1)],[(1,0), (0,1), (1,1), (2,1)]]
for row in range(NUM_ROW):
    for col in range(NUM_COL):
        # ㅗ 꼴을 제외한 나머지는 DFS-백트래킹으로 가능
        visited[row][col] = True
        recursive(row, col, 1, number_map[row][col])
        visited[row][col] = False
        
        # # ㅗ, ㅜ 모양 찾기
        # if row < NUM_ROW - 1 and col < NUM_COL - 2:
        #     for tetro in updown:
        #         tmp = 0
        #         for d_r, d_c in tetro:
        #             tmp += number_map[row + d_r][col + d_c]
        #         max_value[0] = tmp if tmp > max_value[0] else max_value[0]
        # # ㅓ, ㅏ 모양 찾기
        # if row < NUM_ROW - 2 and col < NUM_COL - 1:
        #     for tetro in rightleft:
        #         tmp = 0
        #         for d_r, d_c in tetro:
        #             tmp += number_map[row + d_r][col + d_c]
        #         max_value[0] = tmp if tmp > max_value[0] else max_value[0]   
  
print(max_value[0])