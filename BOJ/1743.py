import sys
sys_input = sys.stdin.readline
sys.setrecursionlimit(10**4)

row, col, num_waste = map(int, sys_input().split(' '))
# 0 
# 1 waste & not visited
# -1 waste % visited
hallway = [[0 for _ in range(col)] for _ in range(row)]
for _ in range(num_waste):
    waste_r, waste_c = map(int, sys_input().split(' '))
    hallway[waste_r-1][waste_c-1] = 1

def dfs(cur_row, cur_col):
    size_waste = 1
    hallway[cur_row][cur_col] = -1
    for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
        next_row, nex_col = cur_row + dr, cur_col + dc
        if 0 <= next_row < row and 0 <= nex_col < col and hallway[next_row][nex_col] == 1:
            size_waste += dfs(next_row, nex_col)
    return size_waste

# MAIN
size_waste = []
for i in range(row):
    for j in range(col):
        if hallway[i][j] == 1:
            size_waste.append(dfs(i, j))
print(max(size_waste))