import sys
sys_input = sys.stdin.readline

NUM_ROW, NUM_COL = map(int, sys_input().strip().split())
matrix_before = [list(map(int, list(sys_input().strip()))) for _ in range(NUM_ROW)]
matrix_after = [list(map(int, list(sys_input().strip()))) for _ in range(NUM_ROW)]
g_num_flips = 0

def flip(r,c):
    global g_num_flips
    g_num_flips += 1
    for i in range(r, r + 3):
        for j in range(c, c + 3):
            if matrix_before[i][j] == 0:
                matrix_before[i][j] = 1
            elif matrix_before[i][j] == 1:
                matrix_before[i][j] = 0

if (NUM_ROW < 3 or NUM_COL < 3) and matrix_before != matrix_after:
    print(-1)
    exit()
for r in range(NUM_ROW - 2):
    for c in range(NUM_COL - 2):
        if matrix_before[r][c] != matrix_after[r][c]:
            flip(r,c)
            
if matrix_before != matrix_after:
    print(-1)
    exit()
else:
    print(g_num_flips)
