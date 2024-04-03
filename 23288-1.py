import sys
sys_input = sys.stdin.readline
from collections import deque

NUM_ROWS, NUM_COLS, NUM_MOVES = map(int, sys_input().split())

board = [list(map(int, sys_input().split())) for _ in range(NUM_ROWS)]
total_point = 0
dice_blueprint = [[0 for _ in range(3)] for _ in range(4)]
dice_blueprint[0][1] = 2
dice_blueprint[1][0] = 4
dice_blueprint[1][1] = 6 # CENTER
dice_blueprint[1][2] = 3
dice_blueprint[2][1] = 5
dice_blueprint[3][1] = 1
dice_row, dice_col, dice_direciton = 0, 0, 1 # 0, 0 EAST

def get_point(start_r, start_c):
    
    global total_point
    
    to_visit = deque([(start_r,start_c)])
    visited = {(start_r,start_c): True}
    start_value = board[start_r][start_c]
    
    while to_visit:
        cur_r, cur_c = to_visit.popleft()
        for d_r, d_c in [(0,1), (0,-1), (1,0), (-1,0)]:
            next_r, next_c = cur_r + d_r, cur_c + d_c
            if 0 <= next_r < NUM_ROWS and 0 <= next_c < NUM_COLS:
                if start_value == board[next_r][next_c] and (next_r, next_c) not in visited:
                    to_visit.append((next_r, next_c))
                    visited[(next_r, next_c)] = True
    
    point = board[start_r][start_c] * len(visited)
    total_point += point

def roll_north():
    global dice_row
    vertical = [dice_blueprint[i][1] for i in range(4)]
    vertical_head = vertical[:3]
    vertical_tail = vertical[3:]
    vertical_tail.extend(vertical_head)
    for i in range(4):
        dice_blueprint[i][1] = vertical_tail[i]
    
    dice_row -= 1
    
def roll_south():
    global dice_row
    vertical = [dice_blueprint[i][1] for i in range(4)]
    vertical_head = vertical[:1]
    vertical_tail = vertical[1:]
    vertical_tail.extend(vertical_head)
    for i in range(4):
        dice_blueprint[i][1] = vertical_tail[i]
    
    dice_row += 1
    
def roll_east():
    global dice_col
    a = dice_blueprint[1][0]
    b = dice_blueprint[3][1]
    c = dice_blueprint[1][2]
    d = dice_blueprint[1][1]
    dice_blueprint[1][0] = d
    dice_blueprint[3][1] = a
    dice_blueprint[1][2] = b
    dice_blueprint[1][1] = c
    dice_col += 1
    
def roll_west():
    global dice_col
    a = dice_blueprint[1][0]
    b = dice_blueprint[3][1]
    c = dice_blueprint[1][2]
    d = dice_blueprint[1][1]
    dice_blueprint[1][0] = b
    dice_blueprint[3][1] = c
    dice_blueprint[1][2] = d
    dice_blueprint[1][1] = a    
    dice_col -= 1

def move_or_rollback():
    global dice_direciton
    if (dice_direciton == 0 and 0 <= dice_row - 1) or (dice_direciton == 2 and dice_row + 1 >= NUM_ROWS):
        # NORTH
        if dice_direciton == 2: dice_direciton = 0
        roll_north()
    elif (dice_direciton == 1 and dice_col + 1 < NUM_COLS) or (dice_direciton == 3 and dice_col - 1 < 0):
        if dice_direciton == 3: dice_direciton = 1
        # EAST
        roll_east()
    elif (dice_direciton == 2 and dice_row + 1 < NUM_ROWS) or (dice_direciton == 0 and dice_row - 1 < 0):
        if dice_direciton == 0: dice_direciton = 2
        # SOUTH
        roll_south()
    elif (dice_direciton == 3 and 0 <= dice_col - 1) or (dice_direciton == 1 and dice_col + 1 >= NUM_COLS):
        # WEST
        if dice_direciton == 1: dice_direciton = 3
        roll_west()
        
def change_direction():
    global dice_direciton
    dice_value = dice_blueprint[1][1]
    board_value = board[dice_row][dice_col]

    if dice_value > board_value:
        # [틀린 코드 남김] 주사위 자체의 방향을 움직이는 줄 알았으나, 이동 방향만 바꾸는 것이었음
        # a = dice_blueprint[0][1]
        # b = dice_blueprint[1][2]
        # c = dice_blueprint[2][1]
        # d = dice_blueprint[1][0] 
        # dice_blueprint[0][1] = d
        # dice_blueprint[1][2] = a
        # dice_blueprint[2][1] = b
        # dice_blueprint[1][0] = c
        dice_direciton = (dice_direciton + 1) % 4
        
    elif dice_value < board_value:
        # [틀린 코드 남김] 주사위 자체의 방향을 움직이는 줄 알았으나, 이동 방향만 바꾸는 것이었음
        # a = dice_blueprint[0][1]
        # b = dice_blueprint[1][2]
        # c = dice_blueprint[2][1]
        # d = dice_blueprint[1][0] 
        # dice_blueprint[0][1] = b
        # dice_blueprint[1][2] = c
        # dice_blueprint[2][1] = d
        # dice_blueprint[1][0] = a
        dice_direciton = (dice_direciton - 1) % 4


# 0 UP(N) 1 RIGHT(E) 2 DOWN(S) 3 LEFT(W)
def movement():
    global dice_row
    global dice_col
    move_or_rollback()
    get_point(dice_row, dice_col)
    change_direction()
    
for _ in range(NUM_MOVES):
    movement()
    
print(total_point)
    
    
    