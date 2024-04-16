#
# 24-03-12
#

# BFS 
# 

import sys
from collections import deque
sys_input = sys.stdin.readline

pos_big, pos_lil = map(int, sys_input().split())

pos_visited = [-1] * 100_001
to_visit = deque()
pos_visited[pos_big] = 0
to_visit.append(pos_big)

while to_visit:
    cur_pos = to_visit.popleft()
    if cur_pos == pos_lil: break
    if cur_pos - 1 >= 0:
        if pos_visited[cur_pos - 1] == -1 or pos_visited[cur_pos - 1] > pos_visited[cur_pos] + 1:
            pos_visited[cur_pos - 1] = pos_visited[cur_pos] + 1
            to_visit.append(cur_pos - 1)
    if cur_pos + 1 <= 100_000:
        if pos_visited[cur_pos + 1] == -1 or pos_visited[cur_pos + 1] > pos_visited[cur_pos] + 1:
            pos_visited[cur_pos + 1] = pos_visited[cur_pos] + 1
            to_visit.append(cur_pos + 1)
    if cur_pos * 2 <= 100_000:
        if pos_visited[cur_pos * 2] == -1 or pos_visited[cur_pos * 2] > pos_visited[cur_pos] + 1:
            pos_visited[cur_pos * 2] = pos_visited[cur_pos] + 1
            to_visit.append(cur_pos * 2)

print(pos_visited[pos_lil])

# 재귀 - Recursive Error
# import sys
# sys_input = sys.stdin.readline

# MAX_POS = 100_000

# min_move = [float('inf')] * (MAX_POS + 1)

# big_bro, lil_bro = map(int, sys_input().split())

# min_move[big_bro] = 0

# def next_move(n):
#     if n-1 >= 0:
#         if min_move[n-1] == -1 or min_move[n-1] > min_move[n] + 1:
#             min_move[n-1] = min_move[n] + 1
#             next_move(n-1)
#     if n+1 <= MAX_POS:
#         if min_move[n+1] == -1 or min_move[n+1] > min_move[n] + 1:
#             min_move[n+1] = min_move[n] + 1
#             next_move(n+1)
#     if 2 * n <= MAX_POS:
#         if min_move[2 * n] == -1 or min_move[2 * n] > min_move[n] + 1:
#             min_move[2 * n] = min_move[n] + 1
#             next_move(2 * n)
    
# next_move(big_bro)
# print(min_move[lil_bro])