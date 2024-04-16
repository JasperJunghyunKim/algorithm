#
# 3트 : 통과
# (엑셀메모 참조)
#

import sys
# import time
sys_input = sys.stdin.readline
SIZE, NUM_INIT_TREES, NUM_YEARS = map(int, sys_input().strip().split())

dead_trees = [[dict() for _ in range(SIZE)] for _ in range(SIZE)]
alive_trees = [[dict() for _ in range(SIZE)] for _ in range(SIZE)]
nutrition = [[5 for _ in range(SIZE)] for _ in range(SIZE)]
add_nutrition = []
num_trees = [[0 for _ in range(SIZE)] for _ in range(SIZE)]


for _ in range(SIZE):
    add_nutrition.append(list(map(int, sys_input().strip().split())))

for _ in range(NUM_INIT_TREES):
    r, c, y = map(int, sys_input().strip().split())
    if y not in alive_trees[r-1][c-1]: alive_trees[r-1][c-1][y] = 0
    alive_trees[r-1][c-1][y] += 1
    num_trees[r-1][c-1] += 1

def spring():
    global alive_trees
    global dead_trees
    new_alive_trees = [[dict() for _ in range(SIZE)] for _ in range(SIZE)]
    new_dead_trees = [[dict() for _ in range(SIZE)] for _ in range(SIZE)]
    
    for r in range(SIZE):
        for c in range(SIZE):
            if num_trees[r][c] == 0: continue
            for y in sorted(alive_trees[r][c].keys()):
                # 전부 성장
                if nutrition[r][c] >= y * alive_trees[r][c][y]:
                    if y + 1 not in new_alive_trees[r][c]: new_alive_trees[r][c][y + 1] = 0
                    new_alive_trees[r][c][y+1] += alive_trees[r][c][y]
                    nutrition[r][c] -= y * alive_trees[r][c][y]
                
                # 전부 죽음 (최소 하나도 성장시킬 수 없다면)
                elif nutrition[r][c] < y:
                    if y not in new_dead_trees[r][c]: new_dead_trees[r][c][y] = 0
                    new_dead_trees[r][c][y] += alive_trees[r][c][y]
                    num_trees[r][c] -= alive_trees[r][c][y]
                
                # 일부 성장, 일부 죽음
                else:
                    n_survive = nutrition[r][c] // y
                    n_die = alive_trees[r][c][y] - n_survive
                    if y + 1 not in new_alive_trees[r][c]: new_alive_trees[r][c][y + 1] = 0
                    new_alive_trees[r][c][y+1] += n_survive
                    nutrition[r][c] -= y * n_survive
                    
                    if y not in new_dead_trees[r][c]: new_dead_trees[r][c][y] = 0
                    new_dead_trees[r][c][y] += n_die
                    num_trees[r][c] -= n_die

    alive_trees = new_alive_trees
    dead_trees = new_dead_trees

def summer():
    for r in range(SIZE):
        for c in range(SIZE):
            for y in dead_trees[r][c].keys():
                nutrition[r][c] += dead_trees[r][c][y] * (y // 2)

def autumn():
    for r in range(SIZE):
        for c in range(SIZE):
            for y in alive_trees[r][c].keys():
                if y % 5 == 0:
                    for dr, dc in [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]:
                        next_r, next_c = r + dr, c + dc
                        if 0 <= next_r < SIZE and 0 <= next_c < SIZE:
                            if 1 not in alive_trees[next_r][next_c]: alive_trees[next_r][next_c][1] = 0
                            alive_trees[next_r][next_c][1] += alive_trees[r][c][y]
                            num_trees[next_r][next_c] += alive_trees[r][c][y]
                        

def winter():
    for r in range(SIZE):
        for c in range(SIZE):
            nutrition[r][c] += add_nutrition[r][c]
            
# t_before = time.time()
for _ in range(NUM_YEARS):
    spring()
    # print("AFTER SPRING")
    # print("ALIVE TREES")
    # print(*alive_trees, sep="\n")
    # print("DEAD TREES")
    # print(*dead_trees, sep="\n")
    # print("NUTRITION TREES")
    # print(*nutrition, sep="\n")


    summer()
    # print("AFTER SUMMER")
    # print(*alive_trees, sep="\n")

    autumn()
    # print("AFTER AUTUMN")
    # print(*alive_trees, sep="\n")

    winter()
    # print("AFTER WINTER")
    # print(*alive_trees, sep="\n")
    # print("NUTRITION TREES")
    # print(*nutrition, sep="\n")


total_num_trees = 0
for r in range(SIZE):
    for c in range(SIZE):
        total_num_trees += num_trees[r][c]
print(total_num_trees)
# print(time.time() - t_before)


#
# 2트 : 시간초과
# 해시테이블(딕셔너리) 사용해봄
# 1트보단 많이 줄었지만 시간초과
#

import sys
# import time
sys_input = sys.stdin.readline
SIZE, NUM_INIT_TREES, NUM_YEARS = map(int, sys_input().strip().split())

dead_trees = [[dict() for _ in range(SIZE)] for _ in range(SIZE)]
alive_trees = [[dict() for _ in range(SIZE)] for _ in range(SIZE)]
nutrition = [[5 for _ in range(SIZE)] for _ in range(SIZE)]
add_nutrition = []
num_trees = [[0 for _ in range(SIZE)] for _ in range(SIZE)]


for _ in range(SIZE):
    add_nutrition.append(list(map(int, sys_input().strip().split())))

for _ in range(NUM_INIT_TREES):
    r, c, y = map(int, sys_input().strip().split())
    if y not in alive_trees[r-1][c-1]: alive_trees[r-1][c-1][y] = 0
    alive_trees[r-1][c-1][y] += 1
    num_trees[r-1][c-1] += 1

def spring():
    global alive_trees
    global dead_trees
    new_alive_trees = [[dict() for _ in range(SIZE)] for _ in range(SIZE)]
    new_dead_trees = [[dict() for _ in range(SIZE)] for _ in range(SIZE)]
    
    for r in range(SIZE):
        for c in range(SIZE):
            if num_trees[r][c] == 0: continue
            for y in sorted(alive_trees[r][c].keys()):
                while alive_trees[r][c][y] > 0:
                    alive_trees[r][c][y] -= 1
                    if nutrition[r][c] >= y:
                        if y + 1 not in new_alive_trees[r][c]: new_alive_trees[r][c][y + 1] = 0
                        new_alive_trees[r][c][y + 1] += 1
                        nutrition[r][c] -= y
                    else:
                        if y not in new_dead_trees[r][c]: new_dead_trees[r][c][y] = 0
                        new_dead_trees[r][c][y] += 1
                        num_trees[r][c] -= 1
    alive_trees = new_alive_trees
    dead_trees = new_dead_trees

def summer():
    for r in range(SIZE):
        for c in range(SIZE):
            for y in dead_trees[r][c].keys():
                nutrition[r][c] += dead_trees[r][c][y] * (y // 2)

def autumn():
    for r in range(SIZE):
        for c in range(SIZE):
            for y in alive_trees[r][c].keys():
                if y % 5 == 0:
                    for dr, dc in [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]:
                        next_r, next_c = r + dr, c + dc
                        if 0 <= next_r < SIZE and 0 <= next_c < SIZE:
                            if 1 not in alive_trees[next_r][next_c]: alive_trees[next_r][next_c][1] = 0
                            alive_trees[next_r][next_c][1] += alive_trees[r][c][y]
                            num_trees[next_r][next_c] += alive_trees[r][c][y]
                        

def winter():
    for r in range(SIZE):
        for c in range(SIZE):
            nutrition[r][c] += add_nutrition[r][c]
            
# t_before = time.time()
for _ in range(NUM_YEARS):
    spring()
    # print("AFTER SPRING")
    # print("ALIVE TREES")
    # print(*alive_trees, sep="\n")
    # print("DEAD TREES")
    # print(*dead_trees, sep="\n")
    # print("NUTRITION TREES")
    # print(*nutrition, sep="\n")


    summer()
    # print("AFTER SUMMER")
    # print(*alive_trees, sep="\n")

    autumn()
    # print("AFTER AUTUMN")
    # print(*alive_trees, sep="\n")

    winter()
    # print("AFTER WINTER")
    # print(*alive_trees, sep="\n")
    # print("NUTRITION TREES")
    # print(*nutrition, sep="\n")


total_num_trees = 0
for r in range(SIZE):
    for c in range(SIZE):
        total_num_trees += num_trees[r][c]
print(total_num_trees)
# print(time.time() - t_before)


#
# 1트 : 시간초과
# 답은 맞음
#


import sys
import time
sys_input = sys.stdin.readline
SIZE, NUM_INIT_TREES, NUM_YEARS = map(int, sys_input().strip().split())

dead_trees = [[[0 for _ in range(1011)] for _ in range(SIZE)] for _ in range(SIZE)]
alive_trees = [[[0 for _ in range(1011)] for _ in range(SIZE)] for _ in range(SIZE)]
nutrition = [[5 for _ in range(SIZE)] for _ in range(SIZE)]
add_nutrition = []
num_trees = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
max_age_alive_tree = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
max_age_dead_tree = [[0 for _ in range(SIZE)] for _ in range(SIZE)]


for _ in range(SIZE):
    add_nutrition.append(list(map(int, sys_input().strip().split())))

for _ in range(NUM_INIT_TREES):
    r, c, y = map(int, sys_input().strip().split())
    alive_trees[r-1][c-1][y] += 1
    num_trees[r-1][c-1] += 1
    max_age_alive_tree[r-1][c-1] = max(max_age_alive_tree[r-1][c-1], y)

def spring():
    global alive_trees
    global dead_trees
    global max_age_alive_tree
    global max_age_dead_tree
    new_alive_trees = [[[0 for _ in range(1011)] for _ in range(SIZE)] for _ in range(SIZE)]
    new_dead_trees = [[[0 for _ in range(1011)] for _ in range(SIZE)] for _ in range(SIZE)]
    new_max_age_alive_tree = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
    new_max_age_dead_tree = [[0 for _ in range(SIZE)] for _ in range(SIZE)]    
    
    for r in range(SIZE):
        for c in range(SIZE):
            for y in range(1, max_age_alive_tree[r][c] + 1):
                if num_trees[r][c] == 0: break
                # 해당 나이의 나무가 있을 때
                while alive_trees[r][c][y] > 0:
                    # 양분이 충분하면
                    if nutrition[r][c] >= y:
                        # 그 나이의 나무를 줄이고
                        # 새 alive 맵에 1 성장한 나무를 추가하고
                        # 양분을 줄입
                        alive_trees[r][c][y] -= 1
                        new_alive_trees[r][c][y+1] += 1
                        new_max_age_alive_tree[r][c] = y + 1
                        nutrition[r][c] -= y
                    else:
                        # 그 나이의 나무를 줄이고
                        # 새 dead 맵에 현재 나이의 나무를 추가
                        # 나무 수를 줄임
                        alive_trees[r][c][y] -= 1
                        new_dead_trees[r][c][y] += 1
                        new_max_age_dead_tree[r][c] = y
                        num_trees[r][c] -= 1

    
    alive_trees = new_alive_trees
    dead_trees = new_dead_trees
    max_age_alive_tree = new_max_age_alive_tree
    max_age_dead_tree = new_max_age_dead_tree    

def summer():
    for r in range(SIZE):
        for c in range(SIZE):
            for y in range(1, max_age_dead_tree[r][c] + 1):
                if dead_trees[r][c][y]:
                    nutrition[r][c] += dead_trees[r][c][y] * (y // 2)

def autumn():
    for r in range(SIZE):
        for c in range(SIZE):
            for y in range(5, max_age_alive_tree[r][c] + 1, 5):
                if alive_trees[r][c][y]:
                    for dr, dc in [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]:
                        next_r, next_c = r + dr, c + dc
                        if 0 <= next_r < SIZE and 0 <= next_c < SIZE:
                            alive_trees[next_r][next_c][1] += alive_trees[r][c][y]
                            num_trees[next_r][next_c] += alive_trees[r][c][y]
                            max_age_alive_tree[next_r][next_c] = max(max_age_alive_tree[next_r][next_c], 1)

def winter():
    for r in range(SIZE):
        for c in range(SIZE):
            nutrition[r][c] += add_nutrition[r][c]
            
t_before = time.time()
for _ in range(NUM_YEARS):
    spring()
    # print("AFTER SPRING")
    # print(*alive_trees, sep="\n")


    summer()
    # print("AFTER SUMMER")
    # print(*alive_trees, sep="\n")

    autumn()
    # print("AFTER AUTUMN")
    # print(*alive_trees, sep="\n")

    winter()
    # print("AFTER WINTER")
    # print(*alive_trees, sep="\n")


total_num_trees = 0
for r in range(SIZE):
    for c in range(SIZE):
        total_num_trees += num_trees[r][c]
print(total_num_trees)
print(time.time() - t_before)
