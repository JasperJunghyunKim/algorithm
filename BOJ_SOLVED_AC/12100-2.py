import sys
sys_input = sys.stdin.readline

SIZE = int(sys_input().strip())
UP, DOWN, RIGHT, LEFT = 0, 1, 2, 3
board = [list(map(int, sys_input().strip().split())) for _ in range(SIZE)]
g_max_block = 0
num_blocks = 0

for r in range(SIZE):
    for c in range(SIZE):
        if board[r][c] > 0: num_blocks += 1

def move_up(num_blocks, new_board):
    def compress_up():    
        for c in range(SIZE):
            row_idx = 0
            for r in range(SIZE):
                if new_board[r][c] != 0:
                    new_board[row_idx][c] = new_board[r][c]
                    if row_idx != r:
                        new_board[r][c] = 0
                    row_idx += 1
    compress_up()
    # collapse
    for c in range(SIZE):
        for r in range(SIZE - 1):
            if new_board[r][c] == new_board[r+1][c]:
                new_board[r][c] *= 2
                new_board[r+1][c] = 0
                num_blocks -= 1
    compress_up()
    return (num_blocks, new_board)
    
def move_down(num_blocks, new_board):
    def compress_down():    
            for c in range(SIZE):
                row_idx = SIZE - 1
                for r in range(SIZE - 1, -1, -1):
                    if new_board[r][c] != 0:
                        new_board[row_idx][c] = new_board[r][c]
                        if row_idx != r:
                            new_board[r][c] = 0
                        row_idx -= 1
    compress_down()
    # collapse
    for c in range(SIZE):
        for r in range(SIZE - 1, 0, -1):
            if new_board[r][c] == new_board[r-1][c]:
                new_board[r][c] *= 2
                new_board[r-1][c] = 0
                num_blocks -= 1
    compress_down()
    return (num_blocks, new_board)

def move_left(num_blocks, new_board):
    def compress_left():
        for r in range(SIZE):
            col_idx = 0
            for c in range(SIZE):
                if new_board[r][c] != 0:
                    new_board[r][col_idx] = new_board[r][c]
                    if col_idx != c:
                        new_board[r][c] = 0
                    col_idx += 1
    compress_left()
    # collapse
    for r in range(SIZE):
        for c in range(SIZE - 1):
            if new_board[r][c] == new_board[r][c+1]:
                new_board[r][c] *= 2
                new_board[r][c+1] = 0
                num_blocks -= 1
    compress_left()
    return (num_blocks, new_board)
    
def move_right(num_blocks, new_board):
    def compress_right():
        for r in range(SIZE):
            col_idx = SIZE - 1
            for c in range(SIZE - 1, -1, -1):
                if new_board[r][c] != 0:
                    new_board[r][col_idx] = new_board[r][c]
                    if col_idx != c:
                        new_board[r][c] = 0
                    col_idx -= 1
    compress_right()
    # collapse
    for r in range(SIZE):
        for c in range(SIZE - 1, 0, -1):
            if new_board[r][c] == new_board[r][c-1]:
                new_board[r][c] *= 2
                new_board[r][c-1] = 0
                num_blocks -= 1
    compress_right()
    return (num_blocks, new_board)
    
def get_max_block(new_board):
    global g_max_block
    for r in range(SIZE):
        for c in range(SIZE):
            g_max_block = new_board[r][c] if new_board[r][c] > g_max_block else g_max_block
            
def backtrack(new_board, num_blocks, num_movements):
    global g_max_block
    if num_blocks == 1 or num_movements == 5:
        get_max_block(new_board)
        return
    
    for i in range(4):
        newnew_board = [i[::] for i in new_board]
        if i == UP:
            num_blocks, newnew_board = move_up(num_blocks, newnew_board)
        elif i == DOWN:
            num_blocks, newnew_board = move_down(num_blocks, newnew_board)
        elif i == RIGHT:
            num_blocks, newnew_board = move_right(num_blocks, newnew_board)
        elif i == LEFT:
            num_blocks, newnew_board = move_left(num_blocks, newnew_board)
        backtrack(newnew_board, num_blocks, num_movements + 1)

backtrack(board, num_blocks, 0)
print(g_max_block)