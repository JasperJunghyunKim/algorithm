import sys
sys_input = sys.stdin.readline
from collections import deque

graph_row, graph_col = map(int, sys_input().split(' '))
graph_before = [list(map(int, sys_input().split(' '))) for _ in range(graph_row)]
graph_after = [list(map(int, sys_input().split(' '))) for _ in range(graph_row)]

def bfs(i, j, pre_color, post_color):
    next_visit = deque()
    graph_before[i][j] = post_color
    next_visit.append((i, j))
    while next_visit:
        cur_row, cur_col = next_visit.popleft()
        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            next_row, next_col = cur_row + dr, cur_col + dc
            if 0 <= next_row < graph_row and 0 <= next_col < graph_col:
                if graph_before[next_row][next_col] == pre_color:
                    graph_before[next_row][next_col] = post_color
                    next_visit.append((next_row, next_col))

is_break = False
for i in range(graph_row):
    for j in range(graph_col):
        if graph_before[i][j] != graph_after[i][j]:
            bfs(i, j, graph_before[i][j], graph_after[i][j])
            is_break = True
            break
    if is_break:
        break

for i in range(graph_row):
    for j in range(graph_col):
        if graph_before[i][j] != graph_after[i][j]:
            print('NO')
            exit()
else:
    print('YES')


# import sys
# sys_input = sys.stdin.readline
# from collections import deque

# graph_row, graph_col = map(int, sys_input().split(' '))
# graph_before = [list(map(int, sys_input().split(' '))) for _ in range(graph_row)]
# graph_after = [list(map(int, sys_input().split(' '))) for _ in range(graph_row)]
# graph_compare = [[0 for _ in range(graph_col)] for _ in range(graph_row)]

# # 변경된 픽셀 유무 찾고 graph_compare 에 표시하기
# # 변경된 픽셀 중 첫번째 찾기
# # 예외케이스 잘 찾아야 함
# # 1. 백신이 퍼졌는데 다른 값으로 업데이트 될 경우
# # 2. 전후 비교를 값 차이로 할 경우, 2 -> 4 된거랑 3 -> 5 된 거를 구분해야되는 경우
# is_changed = False
# first_pixel = tuple()
# first_value = tuple()
# for i in range(graph_row):
#     for j in range(graph_col):
#         if graph_before[i][j] != graph_after[i][j]:
#             if is_changed == False:
#                 first_pixel = (i, j)
#                 first_value = (graph_after[i][j], graph_before[i][j])
#             is_changed = True
#             graph_compare[i][j] = (graph_after[i][j], graph_before[i][j])

# # 전후 차이가 없다면, 백신일 수 있음
# if is_changed == False:
#     print('YES')
#     exit()

# # BFS
# next_visit = deque()
# graph_compare[first_pixel[0]][first_pixel[1]] = 0
# next_visit.append(first_pixel)
# while next_visit:
#     cur_row, cur_col = next_visit.popleft()
#     for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
#         next_row, next_col = cur_row + dr, cur_col + dc
#         if 0 <= next_row < graph_row and 0 <= next_col < graph_col:
#             if graph_compare[next_row][next_col] == first_value:
#                 graph_compare[next_row][next_col] = 0
#                 next_visit.append((next_row, next_col))

# # FIND RESULT
# is_vaccine = True
# for i in range(graph_row):
#     for j in range(graph_col):
#         if graph_compare[i][j] != 0:
#             is_vaccine = False

# if is_vaccine == False:
#     print('NO')
# else:
#     print('YES')

# # Corner Case
# 4 4
# 2 2 2 2
# 2 2 1 3
# 2 1 3 3
# 1 3 3 3
# 4 4 4 4
# 4 4 1 5
# 4 1 5 5
# 1 5 5 5

# 4 4
# 2 2 2 1
# 2 2 1 3
# 2 1 3 3
# 1 3 3 3
# 4 4 4 1
# 7 7 1 3
# 7 1 3 3
# 1 3 3 3
