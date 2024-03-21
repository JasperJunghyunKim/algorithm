#
# 24-03-16
#

import sys
sys_input = sys.stdin.readline

# 4 ~ 500
num_rows, num_cols = map(int, sys_input().split())

number_map = []
for _ in range(num_rows):
    number_map.append(list(map(int, sys_input().split())))
    
visited = [[False for _ in range(num_cols)] for _ in range(num_rows)]

max_value = 0
    
def dfs(cur_row, cur_col, cur_depth, cur_total):
    global max_value
    if cur_depth == 4:
        max_value = cur_total if cur_total > max_value else max_value
        return
        
    for d_r, d_c in [(0,1), (0,-1), (1,0), (-1,0)]:
        next_row, next_col = cur_row + d_r, cur_col + d_c
        if 0 <= next_row < num_rows and 0 <= next_col < num_cols and visited[next_row][next_col] == False:
            # 'ㅗ' 모양에 대한 예외 처리
            if cur_depth == 2:
                visited[next_row][next_col] = True
                dfs(cur_row, cur_col, cur_depth + 1, cur_total + number_map[next_row][next_col])
                visited[next_row][next_col] = False
            visited[next_row][next_col] = True
            dfs(next_row, next_col, cur_depth + 1, cur_total + number_map[next_row][next_col])
            visited[next_row][next_col] = False

# 'ㅗ' 인 경우 해결
def check_exception(cur_row, cur_col):
    global max_value
    for i in range(4):
        tmp = 0
        for k, (d_r, d_c) in enumerate([(-1,0), (0,1), (1,0), (0,-1)]):
            if k == i: continue
            next_row, next_col = cur_row + d_r, cur_col + d_c
            if not (0 <= next_row < num_rows and 0 <= next_col < num_cols):
                break
            else:
                tmp += number_map[next_row][next_col]
        max_value = tmp + number_map[cur_row][cur_col] if tmp + number_map[cur_row][cur_col] > max_value else max_value

for row in range(num_rows):
    for col in range(num_cols):
        visited[row][col] = True
        dfs(row, col, 1, number_map[row][col])
        visited[row][col] = False
        # check_exception(row, col)

print(max_value)