#
# 24-04-10
# 실패코드
#
import sys
sys_input = sys.stdin.readline
NUM_COL, NUM_BRIDGE, NUM_ROW = map(int, sys_input().strip().split())
MAP_SIZE_ROW = 2 * NUM_ROW + 1
MAP_SIZE_COL = 2 * NUM_COL - 1

# INIT MAP
game = [[False for _ in range(2 * NUM_COL - 1)] for _ in range(2 * NUM_ROW + 1)]
for c in range(0, 2 * NUM_COL - 1, 2):
    for r in range(2 * NUM_ROW + 1):
        game[r][c] = True
for _ in range(NUM_BRIDGE):
    a, b = map(int, sys_input().strip().split())
    row = 2 * a - 1
    col = 2 * b - 1
    game[row][col] = True

# GET BRIDE CANDIDATES
bridge_list = []
for r in range(1, MAP_SIZE_ROW, 2):
    for c in range(1, MAP_SIZE_COL, 2): 
        if game[r][c] == False: bridge_list.append((r,c))
# print(bridge_list)
LEN_BRIDGE = len(bridge_list)

# CHECK 
def play_game(start_c):
    end_c = start_c
    for r in range(MAP_SIZE_ROW):
        # 오른쪽이나 왼쪽으로 이동가능하면, 이동
        if end_c + 2 < MAP_SIZE_COL and game[r][end_c + 1]: end_c += 2
        elif end_c - 2 >= 0 and game[r][end_c - 1]: end_c -= 2
    return True if start_c == end_c else False

def cheat_success():
    for c in range(0, MAP_SIZE_COL, 2):
        if not play_game(c):
            return False
    else:
        return True

# Promising
# 놓으려는 곳 오른쪽, 또는 왼쪽에 이미 놓아져 있으면 패스
def is_promising(r, c):
    if c + 2 < MAP_SIZE_COL and game[r][c + 2] == True:
        return False
    if c - 2 >= 0 and game[r][c - 2] == True:
        return False
    return True

# 
def backtrack(num_bridge, idx):
    if 0 <= num_bridge <= 2:
        if cheat_success():
            print(num_bridge)
            exit()
    elif num_bridge == 3:
        if cheat_success():
            print(num_bridge)
            exit()
        else:
            return
    for i in range(idx, LEN_BRIDGE):
        b_r, b_c = bridge_list[i][0], bridge_list[i][1]
        # print(num_bridge)
        # print(b_r, b_c)
        if is_promising(b_r, b_c):
            game[b_r][b_c] = True
            backtrack(num_bridge + 1, i + 1)
            game[b_r][b_c] = False
    
backtrack(0, 0)
print(-1)