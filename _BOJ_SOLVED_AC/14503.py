# ########################################
# # T2
# 문제의 조건 잘 파악 : graph 테두리는 전부 벽이라 했음
# graph[x][y] == -1 을 청소된 조건으로 사용
# 각 방향 0 ~ 3 을 인덱스로 하는 fwd, bwd 배열 사용

import sys
input = sys.stdin.readline

# INIT
row, col = map(int, input().split(' '))
cur_row, cur_col, cur_dir = map(int, input().split(' '))
graph = []
for _ in range(row):
    graph.append(list(map(int, input().split(' '))))

fwd_row = [-1, 0, 1, 0]
fwd_col = [0, 1, 0, -1]
bwd_row = [1, 0, -1, 0]
bwd_col = [0, -1, 0, 1]

# FUNC
def find_adjacent(cur_row, cur_col):
    for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
        next_row, next_col = cur_row + dr, cur_col + dc
        # 상하좌우에 대해 (1) 범위 내 있으며 (2) 벽이 아닌 빈 공간이고 (3 청소되지 않은 경우
        if 0 <= next_row < row and 0 <= next_col < col:
            if graph[next_row][next_col] == 0:
                return True
    return False

# MAIN
cleaner = True
clean_cnt = 0

while cleaner:
    if graph[cur_row][cur_col] == 0:
        graph[cur_row][cur_col] = -1
        clean_cnt += 1
    
    if find_adjacent(cur_row, cur_col):
        cur_dir = (cur_dir + 3) % 4
        if graph[cur_row + fwd_row[cur_dir]][cur_col + fwd_col[cur_dir]] == 0:
            cur_row = cur_row + fwd_row[cur_dir]
            cur_col = cur_col + fwd_col[cur_dir]
    else:
        if graph[cur_row + bwd_row[cur_dir]][cur_col + bwd_col[cur_dir]] == 1:
            cleaner = False
        else:
            cur_row = cur_row + bwd_row[cur_dir]
            cur_col = cur_col + bwd_col[cur_dir]

print(clean_cnt)

# ########################################
# # T1 : 통과했으나 조건문 너무 복잡함
# import sys
# input = sys.stdin.readline

# # INIT
# row, col = map(int, input().split(' '))
# cur_row, cur_col, cur_dir = map(int, input().split(' '))
# graph = []
# cleaned = [[False for _ in range(col)] for _ in range(row)]
# for _ in range(row):
#     graph.append(list(map(int, input().split(' '))))

# # FUNC
# def find_adjacent(cur_row, cur_col):
#     to_clean = False
#     for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
#         next_row, next_col = cur_row + dr, cur_col + dc
#         # 상하좌우에 대해 (1) 범위 내 있으며 (2) 벽이 아닌 빈 공간이고 (3 청소되지 않은 경우
#         if 0 <= next_row < row and 0 <= next_col < col:
#             if graph[next_row][next_col] == 0 and cleaned[next_row][next_col] == False:
#                 to_clean = True
#     return to_clean

# # MAIN
# cleaner = True
# clean_cnt = 0
# while cleaner:
#     if cleaned[cur_row][cur_col] == False:
#         cleaned[cur_row][cur_col] = True
#         clean_cnt += 1
#     # 4군데 중 청소할 빈 칸 있을 경우
#     if find_adjacent(cur_row, cur_col):
#         cur_dir = (cur_dir + 3) % 4
#         if cur_dir == 0:
#             if 0 <= cur_row - 1 < row and graph[cur_row - 1][cur_col] == 0 and cleaned[cur_row - 1][cur_col] == False:
#                 cur_row -= 1
#         elif cur_dir == 1:
#             if 0 <= cur_col + 1 < col and graph[cur_row][cur_col + 1] == 0 and cleaned[cur_row][cur_col + 1] == False:
#                 cur_col += 1
#         elif cur_dir == 2:
#             if 0 <= cur_row + 1 < row and graph[cur_row + 1][cur_col] == 0 and cleaned[cur_row + 1][cur_col] == False:
#                 cur_row += 1
#         elif cur_dir == 3:
#             if 0 <= cur_col - 1 < col and graph[cur_row][cur_col - 1] == 0 and cleaned[cur_row][cur_col - 1] == False:
#                 cur_col -= 1
#     # 다 청소된 경우
#     else:
#         if cur_dir == 0:
#             if 0 <= cur_row + 1 < row and graph[cur_row + 1][cur_col] == 0:
#                 cur_row += 1
#             else:
#                 cleaner = False
#         elif cur_dir == 1:
#             if 0 <= cur_col - 1 < col and graph[cur_row][cur_col - 1] == 0:
#                 cur_col -= 1
#             else:
#                 cleaner = False
#         elif cur_dir == 2:
#             if 0 <= cur_row - 1 < row and graph[cur_row - 1][cur_col] == 0:
#                 cur_row -= 1
#             else:
#                 cleaner = False
#         elif cur_dir == 3:
#             if 0 <= cur_col + 1 < col and graph[cur_row][cur_col + 1] == 0:
#                 cur_col += 1
#             else:
#                 cleaner = False

# print(clean_cnt)