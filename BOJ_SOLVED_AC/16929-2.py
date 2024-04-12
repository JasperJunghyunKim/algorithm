import sys
sys_input = sys.stdin.readline
from collections import deque

NUM_ROW, NUM_COL = map(int, sys_input().strip().split())
board = []
visited = [[0 for _ in range(NUM_COL)] for _ in range(NUM_ROW)]
for _ in range(NUM_ROW):
    board.append(list(sys_input().strip()))

print(visited)
print(board)
is_cycle = False

# make set
root = [[(0,0) for _ in range(NUM_COL)] for _ in range(NUM_ROW)]
for r in range(NUM_ROW):
    for c in range(NUM_COL):
        root[r][c] = (r,c)

# union


for r in range(NUM_ROW):
    for c in range(NUM_COL):
        if is_cycle: break
        if visited[r][c] == 0:
            # DO BFS
            visited[r][c] = 1
            to_visit = deque([(r,c,1)])
            while to_visit:
                if is_cycle: break
                cur_r, cur_c, cur_cnt = to_visit.popleft()
                for dr, dc in [(0,1), (1,0), (-1,0), (0,-1)]:
                    next_r, next_c = cur_r + dr, cur_c + dc
                    # 범위 내
                    # 같은 색깔
                    if 0 <= next_r < NUM_ROW and 0 <= next_c < NUM_COL:
                        if board[next_r][next_c] == board[cur_r][cur_c]:
                            # 방문하지 않은 것이라면
                            if visited[next_r][next_c] == 0:
                                visited[next_r][next_c] = cur_cnt + 1
                                to_visit.append((next_r, next_c, cur_cnt + 1))
                            # 방문된 것 중에 차이가 3이라면 -> 사이클로 판별
                            elif abs(visited[next_r][next_c] - visited[cur_r][cur_c]) >= 3:
                                is_cycle = True
                                break

if is_cycle:
    print('Yes')
else:
    print('No')
                        
                        