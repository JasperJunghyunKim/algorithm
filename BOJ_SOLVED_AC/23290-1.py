import sys
sys_input = sys.stdin.readline

NUM_FISH, NUM_PRACTICE = map(int, sys_input().split())

# 1 ~ 8
directions = [(0,0), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1)]
temp_map = [[[] for _ in range(5)] for _ in range(5)]
game_map = [[[] for _ in range(5)] for _ in range(5)]
smell_map = [[[False for _ in range(5)] for _ in range(5)] for _ in range(NUM_PRACTICE)]
current_practice = 0
for _ in range(NUM_FISH):
    r, c, d = map(int, sys_input().split())
    game_map[r][c].append(d)
shark_row, shark_col = map(int, sys_input().split())

shark_directions = [(-1,0), (0,-1), (1,0), (0,1)]
visited = []
max_path = []
max_value = 0
temp_path = []
temp_value = 0
    
    
def fish_moves(current_practice):
    
    global game_map
    global temp_map
    
    for cur_r in range(1,5):
        for cur_c in range(1,5):
            for cur_d in game_map[cur_r][cur_c]:
                for d_d in range(7):
                    next_d = cur_d - d_d + 8 if cur_d - d_d <= 0 else cur_d - d_d
                    d_r = directions[next_d][0]
                    d_c = directions[next_d][1]
                    next_r = cur_r + d_r
                    next_c = cur_c + d_c
                    if 1 <= next_r <= 4 and 1 <= next_c <= 4:
                        # if smell_map[next_r][next_c] == False and next_r != shark_row and next_c != shark_col:
                        if current_practice - 2 >= 0:
                            if smell_map[current_practice - 2][next_r][next_c] == False or smell_map[current_practice - 1][next_r][next_c] == False:
                                if (next_r, next_c) != (shark_row, shark_col):
                                    temp_map[next_r][next_c].append(next_d)
                                    # print(next_r, next_c, next_d)
                                    break
                        elif current_practice - 1 >= 0:
                            if smell_map[current_practice - 1][next_r][next_c] == False:
                                if (next_r, next_c) != (shark_row, shark_col):
                                    temp_map[next_r][next_c].append(next_d)
                                    # print(next_r, next_c, next_d)
                                    break
                        else:
                            if (next_r, next_c) != (shark_row, shark_col):
                                temp_map[next_r][next_c].append(next_d)
                                # print(next_r, next_c, next_d)
                                break
                else:
                    temp_map[cur_r][cur_c].append(cur_d)
    game_map = temp_map[::]
    temp_map = [[[] for _ in range(5)] for _ in range(5)]
               
               
               
def shark_moves(cur_r, cur_c):
    
    global temp_value
    global temp_path
    global max_value
    global max_path
    
    
    # 최대값 비교
        # 더 클 경우 바로 갱신
        # 같을 경우 moves 비교
    if len(visited) == 3:
        if temp_value > max_value:
            max_path = temp_path[::]
            max_value = temp_value
        elif temp_value == max_value and temp_path < max_path:
            max_path = temp_path[::]
        return
    
    for k, (d_r, d_c) in enumerate(shark_directions):
        next_r = cur_r + d_r
        next_c = cur_c + d_c
        if 1 <= next_r <= 4 and 1 <= next_c <= 4:
            if (next_r, next_c) not in visited:
                visited.append((next_r, next_c))
                temp_path.append(k)
                temp_value += len(game_map[next_r][next_c])
                shark_moves(next_r, next_c)
                visited.pop()
                temp_path.pop()
                temp_value -= len(game_map[next_r][next_c])

def magic(current_practice):
    
    global shark_row
    global shark_col
    dup_map = game_map[::]
    
    # fish
    fish_moves(current_practice)

    # shark moves, eliminate, smell
    shark_moves(shark_row, shark_col)
    # print(max_path)
    for d in max_path:
        shark_row += shark_directions[d][0]
        shark_col += shark_directions[d][1]
        game_map[shark_row][shark_col] = []
        smell_map[current_practice][shark_row][shark_col] = True
        
    # duplicate fish
    for r in range(1,5):
        for c in range(1,5):
            game_map[r][c].extend(dup_map[r][c])
    
    
    
for current_practice in range(NUM_PRACTICE):
    magic(current_practice)

cnt = 0
for r in range(1,5):
    for c in range(1,5):
        cnt += len(game_map[r][c])
print(cnt)

