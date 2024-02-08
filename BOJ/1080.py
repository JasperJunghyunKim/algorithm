import sys
sys_input = sys.stdin.readline
row, col = map(int, sys_input().split(' '))

def flip(row, col):
    for i in range(row, row+3):
        for j in range(col, col+3):
            comparison[i][j] = not comparison[i][j]

pre_matrix = [list(sys_input().strip()) for _ in range(row)]
post_matrix = [list(sys_input().strip()) for _ in range(row)]
comparison = [[False for _ in range(col)] for _ in range(row)]
for i in range(row):
    for j in range(col):
        if pre_matrix[i][j] != post_matrix[i][j]: comparison[i][j] = True

if row < 3 or row < 3:
    print(-1)
    exit()
else:
    cnt = 0
    for i in range(row-2):
        for j in range(col-2):
            if comparison[i][j] == True: 
                cnt+= 1 
                flip(i, j)
    for i in range(row):
        for j in range(col):
            if comparison[i][j] == True:
                print(-1)
                exit()
    print(cnt)