########################################
# T2
import sys
input = sys.stdin.readline
from collections import deque

def distance(pos_a, pos_b):
    return abs(pos_a[0] - pos_b[0]) + abs(pos_a[1] - pos_b[1])

for _ in range(int(input())):
    # INIT
    num_cvs = int(input())
    cvs = []
    visited = [False] * num_cvs
    house_x, house_y = map(int, input().split(' '))
    for _ in range(num_cvs):
        cvs.append(tuple(map(int, input().split(' '))))
    pent_x, pent_y = map(int, input().split(' '))
    to_visit = deque()

    # MAIN
    to_visit.append((house_x, house_y))
    while to_visit:
        cx, cy = to_visit.popleft()
        # 현위치에서 PENT 까지 한번에 갈 수 있으면 happy
        if distance((cx, cy), (pent_x, pent_y)) <= 1000:
            print('happy')
            break
        for i, (nx, ny) in enumerate(cvs):
            if visited[i] == False:
                if distance((cx, cy), (nx, ny)) <= 1000:
                    to_visit.append((nx, ny))
                    visited[i] = True
    else:
        print('sad')



# ########################################
# # T1 - 정답실패 & 시간초과
# import sys
# input = sys.stdin.readline
# from collections import deque

# num_tc = int(input())
# num_cvs = int(input())

# # adjust position
# def adjust_pos(pos):
#     return pos + 32768

# # find distance between two pos
# def find_distance(pos_a, pos_b):
#     return abs(pos_a[0]-pos_b[0]) + abs(pos_a[1]-pos_b[1])


# # RUN TC
# for _ in range(num_tc):
#     # INIT
#     is_available = False
#     cvs_list = []
#     house = tuple(map(adjust_pos, map(int,input().split(' '))))
#     for _ in range(num_cvs):
#         cvs_list.append(tuple(map(adjust_pos, map(int,input().split(' ')))))
#     pentaport = tuple(map(adjust_pos, map(int,input().split(' '))))
#     to_visit = []
#     visited = []
#     # 
#     # if find_distance(house, pentaport) <= 1000:
#     #     print('happy')
#     #     continue
#     #
#     to_visit.append(house)
#     while to_visit:
#         next_visit = []
#         for cy, cx in to_visit:
#             for i in range(-1000, 1001):
#                 for j in range(-1000, 1001):
#                     # 1. 지도 범위 내 있으며
#                     # 2. cx, cy 에서 거리가 1000 이하이며
#                     # 3. CVS 이며
#                     # 4. not visited 인 경우
#                     ny, nx = cy + i, cx + j
#                     if 0 <= ny < 65_536 and 0 <= nx < 65_536:
#                         if find_distance((cy, cx), (ny, nx)) <= 1000:
#                             if (ny, nx) == pentaport:
#                                 is_available = True
#                             if (ny, nx) in cvs_list:
#                                 if (ny, nx) not in visited:
#                                     next_visit.append((ny, nx))
#                                     visited.append((ny, nx))
#         to_visit = next_visit
#         # print(to_visit)
    
#     if is_available:
#         print('happy')
#     else:
#         print('sad')
    

