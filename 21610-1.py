import sys
sys_input = sys.stdin.readline
SIZE, NUM_CMD = map(int, sys_input().split())
bucket_map = [list(map(int, sys_input().split())) for _ in range(SIZE)]
cmd_list = [tuple((map(int, sys_input().split()))) for _ in range(NUM_CMD)]
directions = [
    (0,0),  # BASE
    (0,-1), # LEFT
    (-1,-1),
    (-1,0),
    (-1,1),
    (0,1),
    (1,1),
    (1,0),
    (1,-1)
    ]

# DICT
cloud = {
    (SIZE - 1, 0): True,
    (SIZE - 1, 1): True,
    (SIZE - 2, 0): True,
    (SIZE - 2, 1): True}

# LEFT 1 ~ 
def move_cloud(direction, distance):
    global cloud
    temp_cloud = dict()
    for cur_r, cur_c in cloud.keys():
        d_r = directions[direction][0] * distance
        d_c = directions[direction][1] * distance
        next_r, next_c = cur_r + d_r, cur_c + d_c
        while next_r < 0 or SIZE <= next_r or next_c < 0 or SIZE <= next_c:
            if next_r < 0: next_r += SIZE
            if SIZE <= next_r: next_r -= SIZE
            if next_c < 0: next_c += SIZE
            if SIZE <= next_c: next_c -= SIZE
        temp_cloud[(next_r, next_c)] = True
    cloud = temp_cloud

def rain():
    for cur_r, cur_c in cloud.keys():
        bucket_map[cur_r][cur_c] += 1
        
def water_copy():
    for cur_r, cur_c in cloud.keys():
        amount = 0
        for d_r, d_c in [(-1,-1), (-1,1), (1,1), (1,-1)]:
            next_r, next_c = cur_r + d_r, cur_c + d_c
            if 0 <= next_r < SIZE and 0 <= next_c < SIZE and bucket_map[next_r][next_c] > 0:
                amount += 1
        bucket_map[cur_r][cur_c] += amount
        
def make_cloud():
    global cloud
    temp_cloud = dict()
    for r in range(SIZE):
        for c in range(SIZE):
            if bucket_map[r][c] >= 2 and (r, c) not in cloud:
                bucket_map[r][c] -= 2
                temp_cloud[(r,c)] = True
    cloud = temp_cloud
    
for direction, distance in cmd_list:
    move_cloud(direction, distance)
    rain()
    water_copy()
    make_cloud()
    
print(sum([sum(i) for i in bucket_map]))