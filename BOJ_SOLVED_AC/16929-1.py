import sys
sys_input = sys.stdin.readline
sys.setrecursionlimit(3000)

NUM_ROW, NUM_COL = map(int, sys_input().strip().split())
board = []
visited = [[0 for _ in range(NUM_COL)] for _ in range(NUM_ROW)]
is_cycle = False
for _ in range(NUM_ROW):
    board.append(list(sys_input().strip()))
    
def dfs(cnt, cur_r, cur_c):
    global is_cycle
    if is_cycle: return
    for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
        next_r, next_c = cur_r + dr, cur_c + dc
        if 0 <= next_r < NUM_ROW and 0 <= next_c < NUM_COL:
            if board[next_r][next_c] == board[cur_r][cur_c]:
                if visited[next_r][next_c] == 0:
                    visited[next_r][next_c] = cnt + 1
                    dfs(cnt + 1, next_r, next_c)
                elif abs(visited[next_r][next_c] - visited[cur_r][cur_c]) >= 3:
                    is_cycle = True
                    return
                    
    

for r in range(NUM_ROW):
    for c in range(NUM_COL):
        if is_cycle: break
        if visited[r][c] == 0:
            visited[r][c] = 1
            dfs(1, r, c)

print("Yes") if is_cycle else print("No")
            

