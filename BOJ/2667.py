########################################
# 다른 사람 풀이 참고
import sys
input = sys.stdin.readline

n = int(input().strip())
town = [[] for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    town[i].extend(list(input().strip()))

moves = [(0,1), (1,0), (0,-1), (-1,0)]

def dfs(cur_house):
    visited[cur_house[0]][cur_house[1]] = True
    for dx, dy in moves:
        next_house_x = cur_house[0] + dx
        next_house_y = cur_house[1] + dy
        if (0 <= next_house_x <n) and (0<= next_house_y <n) and town[next_house_x][next_house_y] == '1':
            dfs((next_house_x, next_house_y))

# result
num_section = 0
for i in range(n):
    for j in range(n):
        if town[i][j] == '1' and visited[i][j] == False:
            num_section += 1
            dfs((i,j))

print(num_section)

# ########################################

# import sys
# input = sys.stdin.readline

# n = int(input().strip())
# town = [[] for _ in range(n)]
# visited = [[False for _ in range(n)] for _ in range(n)]
# for i in range(n):
#     town[i].extend(list(input().strip()))

# def find_next_house(cur_house):
#     next_house = []
#     if cur_house[0] > 0 and town[cur_house[0]-1][cur_house[1]] == '1':
#         next_house.append((cur_house[0]-1, cur_house[1]))
#     if cur_house[1] > 0 and town[cur_house[0]][cur_house[1]-1] == '1':
#         next_house.append((cur_house[0], cur_house[1]-1))
#     if cur_house[0] < n-1 and town[cur_house[0]+1][cur_house[1]] == '1':
#         next_house.append((cur_house[0]+1, cur_house[1]))
#     if cur_house[1] < n-1 and town[cur_house[0]][cur_house[1]+1] == '1':
#         next_house.append((cur_house[0], cur_house[1]+1))
#     return next_house

# def dfs(cur_house):
#     global house_per_section
#     visited[cur_house[0]][cur_house[1]] = True
#     house_per_section += 1
#     for next_house in find_next_house(cur_house):
#         if visited[next_house[0]][next_house[1]] == False:
#             dfs(next_house)

# # result
# num_section = 0
# result = []
# for i in range(n):
#     for j in range(n):
#         if town[i][j] == '1' and visited[i][j] == False:
#             house_per_section = 0
#             num_section += 1
#             dfs((i,j))
#             result.append(house_per_section)

# print(num_section)
# result.sort()
# for i in result:
#     print(i)
            