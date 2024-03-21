########################################
# DFS Recusice - Rec Depth Exceeded
# import sys
# sys.setrecursionlimit(10**5)

# from_pos, to_pos = map(int, input().split())

# visited = [-1] * 100_001

# def dfs(cur_pos, count):
#     visited[cur_pos] = count
#     for i in [cur_pos+1, cur_pos-1, cur_pos*2]:
#         if i < 0 or 100_000 < i:
#             continue
#         elif visited[i] == -1 or visited[i] > count + 1:
#             dfs(i, count+1)

# dfs(from_pos, 0)

# print(visited[to_pos])

########################################
# 시간초과 : 1초
from collections import deque
from_pos, to_pos = map(int, input().split())
visited = [-1] * 100_001
to_visit = deque()

to_visit.append((from_pos, 0))
visited[from_pos] = 0

while to_visit:
    cur_pos, cur_count = to_visit.popleft()
    if cur_pos == to_pos:
        break
    for next_pos in [cur_pos + 1, cur_pos - 1, cur_pos * 2]:
        if next_pos < 0 or 100_000 < next_pos:
            continue
        elif visited[next_pos] == -1 or visited[next_pos] > cur_count + 1:
            to_visit.append((next_pos, cur_count + 1))
            visited[next_pos] = cur_count + 1
print(visited[to_pos])