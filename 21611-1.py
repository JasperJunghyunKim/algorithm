import sys
sys_input = sys.stdin.readline

SIZE_MAP, NUM_BLIZZARD = map(int, sys_input().split())
blast_marvels = [0,0,0,0]
game_map_2d = [list(map(int, sys_input().split())) for _ in range(SIZE_MAP)]
game_map_1d = [0]
blizzard_cmd = [tuple(map(int, sys_input().split()))for _ in range(NUM_BLIZZARD)] # 방향, 거리

# init : 2D -> 1D
# 맵을 단순화하기 위해 2D 지도를 -> 1D 인 선형으로 바꿔서 해결
def transform():
    global game_map_1d
    temp_map = [-1 for _ in range(SIZE_MAP * SIZE_MAP)]
    temp_idx = 0
    cur_row = 0
    cur_col = 0
    # 0 RIGHT, 1 DOWN, 2 LEFT, 3 UP
    cur_dir = 0
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    while True:
        if game_map_2d[cur_row][cur_col] > 0:
            temp_map[temp_idx] = game_map_2d[cur_row][cur_col]
            temp_idx += 1
        game_map_2d[cur_row][cur_col] = -1            
            
        next_dir = cur_dir
        next_row, next_col = cur_row + directions[next_dir][0], cur_col + directions[next_dir][1]
        # exceed edge or already visited
        if next_row < 0 or SIZE_MAP <= next_row or next_col < 0 or SIZE_MAP <= next_col or game_map_2d[next_row][next_col] == -1:
            next_dir = (cur_dir + 1) % 4
            next_row, next_col = cur_row + directions[next_dir][0], cur_col + directions[next_dir][1]

        # next round
        cur_row = next_row
        cur_col = next_col
        cur_dir = next_dir
        if cur_row == ((SIZE_MAP+1)/2 - 1) and cur_col == ((SIZE_MAP+1)/2 - 1):
            break
    

    temp_map = temp_map[:temp_map.index(-1):]
    temp_map.reverse()
    game_map_1d.extend(temp_map)

# do blizzard
def do_blizzard(direction, distance):
    target = []
    # 1 up 2 down 3 left 4 right
    if direction == 1: skip = 7
    elif direction == 2: skip = 3
    elif direction == 3: skip = 1
    elif direction == 4: skip = 5
    for i in range(distance):
        if i == 0:
            target.append(skip)
        else:
            target.append(target[-1] + skip)
        skip += 8
    # 가능한 범위에 대해서만 처리
    for t in target:
        if t < len(game_map_1d):
            # [오류 코드]
            # 직접 파괴하는 것도 '폭발' 에 포함되는 줄 알았음
            # if game_map_1d[t] == 1: blast_one += 1
            # elif game_map_1d[t] == 2: blast_two += 1
            # elif game_map_1d[t] == 3: blast_three += 1
            game_map_1d[t] = -1

# contraction
def contraction():
    global game_map_1d
    game_map_1d = [i for i in game_map_1d if i != -1]
    

def blast_four_marvels():
    for i, v in enumerate(game_map_1d):
        if v == 0 or v == -1: continue
        if i + 3 < len(game_map_1d) and game_map_1d[i] == game_map_1d[i + 1] == game_map_1d[i + 2] == game_map_1d[i + 3]:
            len_common = 1
            n = i
            while True:
                if n + 1 < len(game_map_1d) and game_map_1d[n] == game_map_1d[n + 1]:
                        len_common += 1
                else:
                    break
                n += 1
            if v == 1: blast_marvels[1] += len_common
            elif v == 2: blast_marvels[2] += len_common
            elif v == 3: blast_marvels[3] += len_common
            for k in range(len_common):
                game_map_1d[i + k] = -1

 
def update_marvel():
    global game_map_1d
    temp = [0]
    for i, v in enumerate(game_map_1d):
        if v == 0 or v == -1: continue
        if i + 2 < len(game_map_1d) and game_map_1d[i] == game_map_1d[i + 1] == game_map_1d[i + 2]:
            len_common = 3
        elif i + 1 < len(game_map_1d) and game_map_1d[i] == game_map_1d[i + 1]:
            len_common = 2
        else:
            len_common = 1
        temp.extend([len_common, game_map_1d[i]])
        for k in range(len_common):
            game_map_1d[i + k] = -1
    if len(temp) > (SIZE_MAP * SIZE_MAP):
        temp = temp[:(SIZE_MAP * SIZE_MAP)]
    game_map_1d = temp


transform()
for direction, distance in blizzard_cmd:
    do_blizzard(direction, distance)
    while -1 in game_map_1d:
        contraction()
        blast_four_marvels()
    update_marvel()
print(blast_marvels[1] + blast_marvels[2] * 2 + blast_marvels[3] * 3)


    
                
    
