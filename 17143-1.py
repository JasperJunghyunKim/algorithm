import sys
sys_input = sys.stdin.readline

NUM_ROW, NUM_COL, NUM_SHARKS = map(int, sys_input().strip().split())
speed_map = [[0 for _ in range(NUM_COL)] for _ in range(NUM_ROW)]
SHARK_SPEED = 0
SHARK_DIR = 1
SHARK_SIZE = 2
fishing_map = [[[0, 0, 0] for _ in range(NUM_COL)] for _ in range(NUM_ROW)]
shark_directions = [(-1,0), (1,0), (0,1), (0,-1)]
UP, DOWN, RIGHT, LEFT = 0, 1, 2, 3
for _ in range(NUM_SHARKS):
    r, c, s, d, z = map(int, sys_input().strip().split())
    fishing_map[r-1][c-1][SHARK_SPEED] = s
    fishing_map[r-1][c-1][SHARK_DIR] = d - 1
    fishing_map[r-1][c-1][SHARK_SIZE] = z
    
def move_shark():
    global fishing_map
    new_fishing_map = [[[0, 0, 0] for _ in range(NUM_COL)] for _ in range(NUM_ROW)]
    for r in range(NUM_ROW):
        for c in range(NUM_COL):
            shark_speed = fishing_map[r][c][SHARK_SPEED]
            shark_dir = fishing_map[r][c][SHARK_DIR]
            if shark_dir == UP or shark_dir == DOWN:
                shark_speed = shark_speed % (2 * NUM_ROW - 2)
            elif shark_dir == RIGHT or shark_dir == LEFT:
                shark_speed = shark_speed % (2 * NUM_COL - 2)
            shark_size = fishing_map[r][c][SHARK_SIZE]
            next_r, next_c = r + (shark_directions[shark_dir][0] * shark_speed), c + (shark_directions[shark_dir][1] * shark_speed)
            # 격자 범위가 될때까지 이동하고, 방향을 전환해준다
            while not (0 <= next_r < NUM_ROW and 0 <= next_c < NUM_COL):
                if next_r >= NUM_ROW: 
                    next_r = (2 * NUM_ROW) - next_r - 2
                    shark_dir = UP
                    # if shark_dir == UP: shark_dir = DOWN
                    # elif shark_dir == DOWN: shakr_dir = UP
                if next_c >= NUM_COL: 
                    next_c = (2 * NUM_COL) - next_c - 2
                    shark_dir = LEFT
                    # if shark_dir == RIGHT: shark_dir = LEFT
                    # elif shark_dir == LEFT: shakr_dir = RIGHT
                if next_r < 0: 
                    next_r *= -1
                    shark_dir = DOWN
                    # if shark_dir == UP: shark_dir = DOWN
                    # elif shark_dir == DOWN: shakr_dir = UP
                if next_c < 0: 
                    next_c *= -1
                    shark_dir = RIGHT
                    # if shark_dir == RIGHT: shark_dir = LEFT
                    # elif shark_dir == LEFT: shakr_dir = RIGHT
            # 비교 후 상어 배치
            # 이 상어가 기존 상어보다 크다면
            if shark_size > new_fishing_map[next_r][next_c][SHARK_SIZE]:
                new_fishing_map[next_r][next_c][SHARK_SPEED] = shark_speed
                new_fishing_map[next_r][next_c][SHARK_DIR] = shark_dir
                new_fishing_map[next_r][next_c][SHARK_SIZE] = shark_size
        
    fishing_map = new_fishing_map
            
# print(*fishing_map, sep="\n")
shark_size_total = 0    
for fisher_c in range(0, NUM_COL):
    # 땅과 가장 가까운 상어를 잡는다
    for r in range(NUM_ROW):
        if fishing_map[r][fisher_c][SHARK_SIZE] >= 1:
            shark_size_total += fishing_map[r][fisher_c][SHARK_SIZE]
            fishing_map[r][fisher_c][SHARK_SPEED] = 0
            fishing_map[r][fisher_c][SHARK_DIR] = 0
            fishing_map[r][fisher_c][SHARK_SIZE] = 0
            break
    # print("AFTER FISHING")
    # print(*fishing_map, sep="\n")
    # 상어가 이동한다
    move_shark()
    # print("AFTER MOVE")
    # print(*fishing_map, sep="\n")

print(shark_size_total)
        