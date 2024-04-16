import sys
sys_input = sys.stdin.readline
import math


N = int(sys_input().strip())
tornado_map = [list(map(int, sys_input().strip().split())) for _ in range(N)]
tornado_movement = []
direction = [(0,1), (1,0), (0,-1), (-1,0)]
total_loss = 0

def get_tornado_movement():
    visited = [[False for _ in range(N)] for _ in range(N)]
    
    # INIT
    reversed_movement = [(0,0)]
    cur_r, cur_c, cur_d = 0, 0, 0
    visited[cur_r][cur_c] = True
    center = math.floor((N / 2 + 0.5)) - 1
    
    while True:
        if cur_r == center and cur_c == center:
            return list(reversed(reversed_movement))
        next_r, next_c, next_d = cur_r + direction[cur_d][0], cur_c + direction[cur_d][1], cur_d
        
        # if OUT OF RANGE || VISITED below, turn clockwise
        if next_r < 0 or N <= next_r or next_c < 0 or N <= next_c or visited[next_r][next_c]:
            next_d = (cur_d + 1) % 4
            next_r, next_c = cur_r + direction[next_d][0], cur_c + direction[next_d][1]
        
        reversed_movement.append((next_r, next_c))   
        visited[next_r][next_c] = True
        cur_r, cur_c, cur_d = next_r, next_c, next_d

tornado_movement = get_tornado_movement()

ROW = 0
COL = 1
for i in range(0, len(tornado_movement) - 1):

    from_pos = tornado_movement[i]
    to_pos = tornado_movement[i + 1]
    
    straight_d_r = to_pos[ROW] - from_pos[ROW]
    straight_d_c = to_pos[COL] - from_pos[COL]
    straight_idx = direction.index((straight_d_r, straight_d_c))

    alpha = (to_pos[ROW] + straight_d_r, to_pos[COL] + straight_d_c)
    five = (alpha[ROW] + straight_d_r, alpha[COL] + straight_d_c, 0.05)
    
    # right d_r, d_c
    right_d_r = direction[(straight_idx + 1) % 4][ROW]
    right_d_c = direction[(straight_idx + 1) % 4][COL]
    r_10 = (alpha[ROW] + right_d_r, alpha[COL] + right_d_c, 0.1)
    r_7 = (to_pos[ROW] + right_d_r, to_pos[COL] + right_d_c, 0.07)
    r_2 = (to_pos[ROW] + right_d_r * 2, to_pos[COL] + right_d_c * 2, 0.02)
    r_1 = (from_pos[ROW] + right_d_r, from_pos[COL] + right_d_c, 0.01)
    
    # left d_r, d_c
    left_d_r = direction[(straight_idx + 3) % 4][ROW]
    left_d_c = direction[(straight_idx + 3) % 4][COL]
    l_10 = (alpha[ROW] + left_d_r, alpha[COL] + left_d_c, 0.1)
    l_7 = (to_pos[ROW] + left_d_r, to_pos[COL] +left_d_c, 0.07)
    l_2 = (to_pos[ROW] + left_d_r * 2, to_pos[COL] + left_d_c * 2, 0.02)
    l_1 = (from_pos[ROW] + left_d_r, from_pos[COL] + left_d_c, 0.01)
    
    # other than alpha
    to_pos_total = tornado_map[to_pos[ROW]][to_pos[COL]]
    removed_total = 0
    for r, c, pcnt in [five, l_10, l_7, l_2, l_1, r_10, r_7, r_2, r_1]:
        scoop = math.floor(to_pos_total * pcnt)
        # 격자 안이면 축적
        if 0 <= r < N and 0 <= c < N:
            tornado_map[r][c] += scoop
        # 격자 밖이면 손실
        else:
            total_loss += scoop
        removed_total +=scoop
    
    # alpha
    if 0 <= alpha[ROW] < N and 0 <= alpha[COL] < N:
        tornado_map[alpha[ROW]][alpha[COL]] += (to_pos_total - removed_total)
    else:
        total_loss += (to_pos_total - removed_total)
    tornado_map[to_pos[ROW]][to_pos[COL]] = 0


print(total_loss)