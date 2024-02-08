import sys
sys_input = sys.stdin.readline

height, width = map(int, sys_input().split(' '))
graph = [list(sys_input().strip()) for _ in range(height)]
parent_pixel = [[(i ,j) for j in range(width)] for i in range(height)]
visited = [[False for _ in range(width)] for _ in range(height)]

def find_root(row, col):
    if parent_pixel[row][col] == (row, col): return (row, col)
    parent_pixel[row][col] = find_root(*parent_pixel[row][col])
    return parent_pixel[row][col]

def union(row1, col1, row2, col2):
    (row1, col1) = find_root(row1, col1)
    (row2, col2) = find_root(row2, col2)
    if (row1, col1) == (row2, col2): return
    parent_pixel[row2][col2] = (row1, col1)
    return

def dfs(root_row, root_col, cur_row, cur_col):
    visited[cur_row][cur_col] = True
    union(root_row, root_col, cur_row, cur_col)
    for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
        next_row, next_col = cur_row + dr, cur_col + dc
        # in range
        # same color
        # root itself
        if 0 <= next_row < height and 0 <= next_col < width:
            if graph[cur_row][cur_col] == graph[next_row][next_col]:
                if find_root(next_row, next_col) == (next_row, next_col):
                    if (next_row, next_col) == (root_row, root_col): continue
                    return dfs(root_row, root_col, next_row, next_col)
                else: 
                    if find_root(next_row, next_col) == (root_row, root_col):
                        return True
                # elif find_root(next_row, next_col) == (root_row, root_col):
                #     return True

for i in range(height):
    for j in range(width):
        if (i, j) == find_root(i, j):
            if dfs(i, j, i, j) == True:
                print('Yes')
                exit()
print('No')