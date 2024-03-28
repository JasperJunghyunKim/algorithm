# 
# 24-03-28
# BackTracking
# 
import sys
sys_input = sys.stdin.readline
sudoku = [list(map(int, sys_input().strip().split())) for _ in range(9)]
missing_cells = []

def check_row(row):
    numbers = [False] * 9
    for col in range(9):
        if sudoku[row][col]:
            numbers[sudoku[row][col] - 1] = True
    if numbers.count(False) == 1:
        return numbers.index(False) + 1
    else:
        return 0
    
def check_col(col):
    numbers = [False] * 9
    for row in range(9):
        if sudoku[row][col]:
            numbers[sudoku[row][col] - 1] = True
    if numbers.count(False) == 1:
        return numbers.index(False) + 1
    else:
        return 0
    
def check_square(row, col):
    left_top_row = (row // 3) * 3
    left_top_col = (col // 3) * 3
    numbers = [False] * 9
    for r in range(left_top_row, left_top_row + 3):
        for c in range(left_top_col, left_top_col +3):
            if sudoku[r][c]:
                numbers[sudoku[row][col] - 1] = True
                
    if numbers.count(False) == 1:
        return numbers.index(False) + 1
    else:
        return 0
    
def get_candid(row, col):
    numbers = [False] * 10
    left_top_row = (row // 3) * 3
    left_top_col = (col // 3) * 3
    for i in range(9):
        if sudoku[row][i]:
            numbers[sudoku[row][i]] = True
        if sudoku[i][col]:
            numbers[sudoku[i][col]] = True
    for r in range(left_top_row, left_top_row + 3):
        for c in range(left_top_col, left_top_col +3):
            if sudoku[r][c]:
                numbers[sudoku[r][c]] = True
    
    numbers = [k for k, v in enumerate(numbers) if k != 0 and v == False]

    return numbers
    
for r in range(9):
    for c in range(9):
        if sudoku[r][c] == 0: 
            # # check row 
            # tmp = check_row(r)
            # if tmp:
            #     sudoku[r][c] = tmp
            #     continue
            # # check col
            # tmp = check_col(c)
            # if tmp:
            #     sudoku[r][c] = tmp
            #     continue                
            # # check square
            # tmp = check_square(r,c)
            # if tmp:
            #     sudoku[r][c] = tmp
            #     continue      
            missing_cells.append((r, c))
            
# 
def recursive(idx):
    if idx == len(missing_cells) - 1:
        for k in sudoku:
            print(*k, sep=' ')
        exit()
    next_r, next_c = missing_cells[idx + 1]
    candidates = get_candid(next_r, next_c)
    for number in candidates:
        sudoku[next_r][next_c] = number
        recursive(idx + 1)
        sudoku[next_r][next_c] = 0

if missing_cells:
    r, c = missing_cells[0]
    candidates = get_candid(r, c)
    for number in candidates:
        sudoku[r][c] = number
        recursive(0)
        sudoku[r][c] = 0
else:
    for k in sudoku:
        print(*k, sep=' ')
     