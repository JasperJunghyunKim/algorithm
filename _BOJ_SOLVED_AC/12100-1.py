#
# 틀림
#

import sys
sys_input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10000)

SIZE_BOARD = int(sys_input())
board = [list(map(int, sys_input().split())) for _ in range(SIZE_BOARD)]
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
directions = [LEFT, RIGHT, UP, DOWN]
max_val = 0

def move_left(board):
    new_board = []
    for r in range(SIZE_BOARD):
        tmp_row = []
        is_doublable = True
        for c in range(SIZE_BOARD):
            if board[r][c] == 0:
                continue
            if not tmp_row:
                tmp_row.append(board[r][c])
            else:
                if board[r][c] != 0 and board[r][c] == tmp_row[len(tmp_row) - 1] and is_doublable:
                    tmp_row[len(tmp_row) - 1] *= 2
                    is_doublable = False
                elif board[r][c] != 0 and board[r][c] == tmp_row[len(tmp_row) - 1] and not is_doublable:
                    tmp_row.append(board[r][c])
                    is_doublable = True
                elif board[r][c] != 0 and board[r][c] != tmp_row[len(tmp_row) - 1]:
                    tmp_row.append(board[r][c])
                    is_doublable = True
        tmp_row.extend([0] * (SIZE_BOARD - len(tmp_row)))
        new_board.append(tmp_row)
    return new_board
            
def move_right(board):
    new_board = []
    for r in range(SIZE_BOARD):
        tmp_row = []
        is_doublable = True
        for c in range(SIZE_BOARD)[::-1]:
            if board[r][c] == 0:
                continue
            if not tmp_row:
                tmp_row.append(board[r][c])
            else:
                if board[r][c] == tmp_row[len(tmp_row) - 1] and is_doublable:
                    tmp_row[len(tmp_row) - 1] *= 2
                    is_doublable = False
                elif board[r][c] == tmp_row[len(tmp_row) - 1] and not is_doublable:
                    tmp_row.append(board[r][c])
                    is_doublable = True
                elif board[r][c] != tmp_row[len(tmp_row) - 1]:
                    tmp_row.append(board[r][c])
                    is_doublable = True
        tmp_row.extend([0] * (SIZE_BOARD - len(tmp_row)))
        new_board.append(list(reversed(tmp_row)))
    return new_board

def move_up(board):
    new_board = [i[::] for i in board]
    for c in range(SIZE_BOARD):
        tmp_col = []
        is_doublable = True
        for r in range(SIZE_BOARD):
            if board[r][c] == 0:
                continue
            if not tmp_col:
                tmp_col.append(board[r][c])
            else:
                if board[r][c] == tmp_col[len(tmp_col) - 1] and is_doublable:
                    tmp_col[len(tmp_col) - 1] *= 2
                    is_doublable = False
                elif board[r][c] == tmp_col[len(tmp_col) - 1] and not is_doublable:
                    tmp_col.append(board[r][c])
                    is_doublable = True
                elif board[r][c] != tmp_col[len(tmp_col) - 1]:
                    tmp_col.append(board[r][c])
                    is_doublable = True
        tmp_col.extend([0] * (SIZE_BOARD - len(tmp_col)))
        for r in range(SIZE_BOARD):
            new_board[r][c] = tmp_col[r]
    return new_board

def move_down(board):
    new_board = [i[::] for i in board]
    for c in range(SIZE_BOARD):
        tmp_col = []
        is_doublable = True
        for r in range(SIZE_BOARD)[::-1]:
            if board[r][c] == 0:
                continue
            if not tmp_col:
                tmp_col.append(board[r][c])
            else:
                if board[r][c] != 0 and board[r][c] == tmp_col[len(tmp_col) - 1] and is_doublable:
                    tmp_col[len(tmp_col) - 1] *= 2
                    is_doublable = False
                elif board[r][c] != 0 and board[r][c] == tmp_col[len(tmp_col) - 1] and not is_doublable:
                    tmp_col.append(board[r][c])
                    is_doublable = True
                elif board[r][c] != 0 and board[r][c] != tmp_col[len(tmp_col) - 1]:
                    tmp_col.append(board[r][c])
                    is_doublable = True
        tmp_col.extend([0] * (SIZE_BOARD - len(tmp_col)))
        tmp_col.reverse()
        for r in range(SIZE_BOARD):
            new_board[r][c] = tmp_col[r]
    return new_board


def recursive(d, num_moves, board):
    global max_val
    new_board = None
    if d == LEFT:
        new_board = move_left(board)
    elif d == RIGHT:
        new_board = move_right(board)
    elif d == UP:
        new_board = move_up(board)
    elif d == DOWN:
        new_board = move_down(board)
    num_moves += 1
    if num_moves == 5:
        max_new_board = max([max(i) for i in new_board])
        max_val = max_new_board if max_new_board > max_val else max_val
        return
    for d in range(4):
        recursive(d, num_moves + 1, new_board)
        
    
for d in directions:
    recursive(d, 0, board)
    
print(max_val)
    