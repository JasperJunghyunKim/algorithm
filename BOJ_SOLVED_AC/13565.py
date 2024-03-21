import sys
sys_input = sys.stdin.readline
from collections import deque

row, col = map(int, sys_input().split(' '))
fiber = [list(sys_input().strip()) for _ in range(row)]

def bfs(i, j):
    next_visit = deque()
    visited[i][j] = True
    next_visit.append((i, j))
    while next_visit:
        cur_row, cur_col = next_visit.popleft()
        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            next_row, next_col = cur_row + dr, cur_col + dc
            if 0 <= next_row < row and 0 <= next_col < col:
                if fiber[next_row][next_col] == '0' and visited[next_row][next_col] == False:
                    visited[next_row][next_col] = True
                    next_visit.append((next_row, next_col))
    
visited = [[False for _ in range(col)] for _ in range(row)]
for j in range(col):
    if fiber[0][j] == '0' and visited[0][j] == False:
        bfs(0, j)
for j in range(col):
    if visited[row-1][j] == True:
        print('YES')
        break
else:
    print('NO')