import sys
import heapq
sys_input = sys.stdin.readline

NUM_ROW, NUM_COL = map(int, sys_input().split())
factory_map = [list(map(int, sys_input().split())) for _ in range(NUM_ROW)]

# E0 W1 S2 N3
START_R, START_C, START_D = map(lambda x : x-1, map(int, sys_input().split()))
END_R, END_C, END_D = map(lambda x : x-1, map(int, sys_input().split()))

def turn_left(cur_dir):
    if cur_dir == 0:
        return 3
    elif cur_dir == 1:
        return 2
    elif cur_dir == 2:
        return 0
    elif cur_dir == 3:
        return 1
    
def turn_right(cur_dir):
    if cur_dir == 0:
        return 2
    elif cur_dir == 1:
        return 3
    elif cur_dir == 2:
        return 1
    elif cur_dir == 3:
        return 0
    
def get_fwd_moves(cur_dir, cur_row, cur_col):
    next_pos = []
    moves = [(0,1), (0,-1), (1,0), (-1,0)]
    next_row, next_col = cur_row, cur_col
    for _ in range(3):
        next_row, next_col = next_row + moves[cur_dir][0], next_col + moves[cur_dir][1]
        if 0 <= next_row < NUM_ROW and 0 <= next_col < NUM_COL and factory_map[next_row][next_col] == 0:
            next_pos.append((cur_dir, next_row, next_col))
        else:
            break
    return next_pos

def dijkstra(start_r, start_c, start_d):
    commands = [[[float('inf') for _ in range(NUM_COL)] for _ in range(NUM_ROW)] for _ in range(4)]
    commands[start_d][start_r][start_c] = 0
    pq = [(0, start_d, start_r, start_c)]
    
    while pq:
        min_commands, min_d, min_r, min_c = heapq.heappop(pq)
        if min_commands > commands[min_d][min_r][min_c]: 
            continue
        else:
            # turn left
            next_r, next_c, next_d = min_r, min_c, turn_left(min_d)
            if commands[next_d][next_r][next_c] > commands[min_d][min_r][min_c] + 1:
                commands[next_d][next_r][next_c] = commands[min_d][min_r][min_c] + 1
                heapq.heappush(pq, (commands[min_d][min_r][min_c] + 1, next_d, next_r, next_c))
            
            # turn right
            next_r, next_c, next_d = min_r, min_c, turn_right(min_d)
            if commands[next_d][next_r][next_c] > commands[min_d][min_r][min_c] + 1:
                commands[next_d][next_r][next_c] = commands[min_d][min_r][min_c] + 1
                heapq.heappush(pq, (commands[min_d][min_r][min_c] + 1, next_d, next_r, next_c))
            
            # move fwd 1 ~ 3
            for next_d, next_r, next_c in get_fwd_moves(min_d, min_r, min_c):
                if commands[next_d][next_r][next_c] > commands[min_d][min_r][min_c] + 1:
                    commands[next_d][next_r][next_c] = commands[min_d][min_r][min_c] + 1
                    heapq.heappush(pq, (commands[min_d][min_r][min_c] + 1, next_d, next_r, next_c))
            
    return commands

commands = dijkstra(START_R, START_C, START_D)
print(commands[END_D][END_R][END_C])