import sys
sys_input = sys.stdin.readline

NUM_ROW, NUM_COL = map(int, sys_input().strip().split())
RIGHTDOWN, RIGHTUP = 0, 1
g_max_value = 0
board = [list(map(int, sys_input().strip().split())) for _ in range(NUM_ROW)]
visited = [[False] * NUM_COL for _ in range(NUM_ROW)]
direction = [[(0,1), (1,0)], [(0,1), (-1,0)]]

def tetro(length, cur_r, cur_c, cur_sum, d):
    global g_max_value
    if length == 4:
        g_max_value = cur_sum if cur_sum > g_max_value else g_max_value
        return
    for dr, dc in direction[d]:
        next_r, next_c = cur_r + dr, cur_c + dc
        if 0 <= next_r < NUM_ROW and 0 <= next_c < NUM_COL:
            if not visited[next_r][next_c]:
                # ㅏ ㅗ ㅓ ㅜ 모양일 때, 길이 2 에서 한번 꺾어주는 단계가 필요
                if length == 2:
                    visited[next_r][next_c] = True
                    tetro(length + 1, cur_r, cur_c, cur_sum + board[next_r][next_c], d)
                    visited[next_r][next_c] = False
                visited[next_r][next_c] = True
                tetro(length + 1, next_r, next_c, cur_sum + board[next_r][next_c], d)
                visited[next_r][next_c] = False


for r in range(NUM_ROW):
    for c in range(NUM_COL):
        visited[r][c] = True
        tetro(0, r, c, 0, RIGHTDOWN)
        tetro(0, r, c, 0, RIGHTUP)
        visited[r][c] = False

# 그외
# 정사각형, ㅓ
for r in range(NUM_ROW - 1):
    for c in range(NUM_COL - 1):
        tmp_sum = board[r][c] + board[r][c+1] + board[r+1][c] + board[r+1][c+1]
        g_max_value = tmp_sum if tmp_sum > g_max_value else g_max_value

for r in range(NUM_ROW - 2):
    for c in range(1, NUM_COL):
        tmp_sum = board[r][c] + board[r+1][c] + board[r+2][c] + board[r+1][c-1]
        g_max_value = tmp_sum if tmp_sum > g_max_value else g_max_value

print(g_max_value)