#
# 24-04-11
# 성공코드 - 단, 시간, 공간 복잡도 개선 필요
#

import sys
sys_input = sys.stdin.readline
NUM_FISH, NUM_CMD = map(int, sys_input().strip().split())
SIZE = 4
fish_map = [[[] for _ in range(SIZE)] for _ in range(SIZE)]
smell_map = [[[False for _ in range(SIZE)] for _ in range(SIZE)] for _ in range(101)]
for _ in range(NUM_FISH):
    fish_r, fish_c, fish_d = map(int, sys_input().strip().split())
    fish_map[fish_r - 1][fish_c - 1].append(fish_d - 1)
shark_r, shark_c = map(int, sys_input().strip().split())
shark_r -= 1
shark_c -= 1

fish_directions = [(0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1)]
shark_directions = [(-1,0), (0,-1), (1,0), (0,1)]

def fish_move(cur_t):
    global fish_map
    fish_map_aftermove = [[[] for _ in range(SIZE)] for _ in range(SIZE)]
    for cur_r in range(SIZE):
        for cur_c in range(SIZE):
            for fish_d in fish_map[cur_r][cur_c]:
                # search all directions
                for i in range(8):
                    next_r, next_c = cur_r + fish_directions[fish_d][0], cur_c + fish_directions[fish_d][1]
                    # 격자 내
                    # 냄새 없음
                    # 상어 아님
                    if 0 <= next_r < SIZE and 0 <= next_c < SIZE:
                        is_smell = False
                        for t in range(cur_t - 2, cur_t):
                            if t < 0: continue
                            if smell_map[t][next_r][next_c]: is_smell = True
                        if not is_smell:
                            if (next_r, next_c) != (shark_r, shark_c):
                                fish_map_aftermove[next_r][next_c].append(fish_d)
                                break
                    # turn 45 deg counter clock
                    fish_d = (fish_d + 7) % 8
                else:
                    # no place to move -> stay
                    fish_map_aftermove[cur_r][cur_c].append(fish_d)
    fish_map = fish_map_aftermove

# return 
def get_shark_path(cur_r, cur_c, cnt, movement, coordinate, eat_fish):
    global max_movement
    global max_coordinate
    global max_eat_fish
    if cnt == 3:
        if eat_fish > max_eat_fish:
            max_eat_fish = eat_fish
            max_movement = movement
            max_coordinate = coordinate
        elif eat_fish == max_eat_fish:
            if movement < max_movement:
                max_movement = movement
                max_coordinate = coordinate
        return
    for shark_d, (dr, dc) in enumerate(shark_directions):
        next_r, next_c = cur_r + dr, cur_c + dc
        if 0 <= next_r < SIZE and 0 <= next_c < SIZE:
            if (next_r, next_c) not in coordinate:
                get_shark_path(next_r, next_c, cnt + 1, movement + [shark_d], coordinate + [(next_r, next_c)], eat_fish + len(fish_map[next_r][next_c]))
            else:
                get_shark_path(next_r, next_c, cnt + 1, movement + [shark_d], coordinate + [(next_r, next_c)], eat_fish)

                            
for t in range(1, NUM_CMD + 1):
    # get copy of current fishmap
    fish_map_duplicate_copy = [[j[::] for j in i] for i in fish_map]
    # print("=========", t, "=========")
    # print("AFTER COPY")
    # print(*fish_map_duplicate_copy, sep="\n")
    # print("shark : ", shark_r, shark_c)
    
    # fish move
    fish_move(t)
    # print("AFTER FISH MOVE")
    # print(*fish_map, sep="\n")
    # print("shark : ", shark_r, shark_c)
    
    
    # shark move, eat fish, leave smell
    max_coordinate = []
    max_movement = [100,100,100]
    max_eat_fish = 0
    get_shark_path(shark_r, shark_c, 0, [], [], 0)
    for r, c in max_coordinate:
        shark_r, shark_c = r, c
        if len(fish_map[shark_r][shark_c]) > 0:
            smell_map[t][shark_r][shark_c] = True
        fish_map[shark_r][shark_c] = []
    # print("AFTER SHARK MOVE")
    # print(*fish_map, sep="\n")
    # print("shark : ", shark_r, shark_c)
    # print(*smell_map[t], sep="\n")
    
    
    # duplicate fish
    for r in range(SIZE):
        for c in range(SIZE):
            fish_map[r][c].extend(fish_map_duplicate_copy[r][c])
    # print("AFTER DUPLICATE")
    # print(*fish_map, sep="\n")
    # print("shark : ", shark_r, shark_c)

total_fish = 0
for r in range(SIZE):
    for c in range(SIZE):
        total_fish += len(fish_map[r][c])
print(total_fish)