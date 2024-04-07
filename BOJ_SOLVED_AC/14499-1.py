import sys
sys_input = sys.stdin.readline

NUM_ROW, NUM_COL, cur_r, cur_c, NUM_CMD = map(int, sys_input().strip().split())
dice_map = [list(map(int, sys_input().strip().split())) for _ in range(NUM_ROW)]
cmd_list = list(map(int, sys_input().strip().split()))
directions = {1: (0,1), 2:(0,-1), 3:(-1,0), 4:(1,0)}
# 주사위 전개도
# 바닥면이 1,1
# 상단면이 3,1
BOTTOM = 0
EAST = 1
WEST = 2
NORTH = 3
SOUTH = 4
TOP = 5
dice = [0,0,0,0,0,0]

def move_north():
    dice[NORTH], dice[BOTTOM], dice[SOUTH], dice[TOP] = dice[TOP], dice[NORTH], dice[BOTTOM], dice[SOUTH]
def move_south():
    dice[NORTH], dice[BOTTOM], dice[SOUTH], dice[TOP] = dice[BOTTOM], dice[SOUTH], dice[TOP], dice[NORTH]
def move_west():
    dice[WEST], dice[BOTTOM], dice[EAST], dice[TOP] = dice[TOP], dice[WEST], dice[BOTTOM], dice[EAST]
def move_east():
    dice[WEST], dice[BOTTOM], dice[EAST], dice[TOP] = dice[BOTTOM], dice[EAST], dice[TOP], dice[WEST]

for cmd in cmd_list:
    next_r, next_c = cur_r + directions[cmd][0], cur_c + directions[cmd][1]
    if next_r < 0 or NUM_ROW <= next_r or next_c < 0 or NUM_COL <= next_c: 
        continue
    if cmd == EAST: move_east()
    elif cmd == WEST: move_west()
    elif cmd == NORTH: move_north()
    elif cmd == SOUTH: move_south()
    
    if dice_map[next_r][next_c] == 0:
        dice_map[next_r][next_c] = dice[BOTTOM]
    else:
        dice[BOTTOM] = dice_map[next_r][next_c]
        dice_map[next_r][next_c] = 0
    
    # 
    print(dice[TOP])
    
    # 
    cur_r, cur_c = next_r, next_c
    