#
# 24-03-15
# T2 
# 예제 결과는 맞으나, 시간 초과
# 3085-1 에서 해결했던 방법대로, 중복 조건 제거 필요
#
import sys
sys_input = sys.stdin.readline

n = int(sys_input().strip())

candy_map = []
 
for _ in range(n):
    candy_map.append(list(sys_input().strip()))
    
def swap(row_a, col_a, row_b, col_b):
    tmp = candy_map[row_a][col_a]
    candy_map[row_a][col_a] = candy_map[row_b][col_b]
    candy_map[row_b][col_b] = tmp
    
# direction(0 ~ 3 : up, right, down, left) 
def find_depth(start_row, start_col, direction):
    size = 1
    next_row = start_row + [(-1,0), (0,1), (1,0), (0,-1)][direction][0]
    next_col = start_col + [(-1,0), (0,1), (1,0), (0,-1)][direction][1]
    while candy_map[start_row][start_col] == candy_map[next_row][next_col]:
        size += 1
        next_row = next_row + [(-1,0), (0,1), (1,0), (0,-1)][direction][0]
        next_col = next_col + [(-1,0), (0,1), (1,0), (0,-1)][direction][1]
        if not (0 <= next_row < n and 0 <= next_col < n):
            break
    return size

# get longest size
def find_longest():
    longest_size = 1    
    for cur_row in range(n):
        for cur_col in range(n):
            for direction, (d_row, d_col) in enumerate([(-1,0), (0,1), (1,0), (0,-1)]):
                next_row, next_col = cur_row + d_row, cur_col + d_col
                if 0 <= next_row < n and 0 <= next_col < n:
                    if candy_map[cur_row][cur_col] == candy_map[next_row][next_col]:
                        size = find_depth(cur_row, cur_col, direction) 
                        longest_size = size if size > longest_size else longest_size
    return longest_size

longest_size = 1
for cur_row in range(n):
    for cur_col in range(n):
        for d_r, d_c in [(0,1), (0,-1), (1,0), (-1,0)]:
            target_row = cur_row + d_r
            target_col = cur_col + d_c
            if 0 <= target_row < n and 0 <= target_col < n:
                swap(cur_row, cur_col, target_row, target_col)
                size = find_longest()
                longest_size = size if size > longest_size else longest_size
                swap(cur_row, cur_col, target_row, target_col)
print(longest_size)

# #
# # T1
# # AABAA 로 되어 있을 때, B 를 swap 하여 AAAAA 가 되는 경우를 고려하지 못함
# # (노가다로 풀었음)
# # 

# import sys
# sys_input = sys.stdin.readline

# n = int(sys_input().strip())

# candy_map = []
 
# for _ in range(n):
#     candy_map.append(list(sys_input().strip()))
    
# # direction(0 ~ 3 : up, right, down, left) 
# def find_depth(start_row, start_col, direction):
#     size = 1
#     next_row = start_row + [(-1,0), (0,1), (1,0), (0,-1)][direction][0]
#     next_col = start_col + [(-1,0), (0,1), (1,0), (0,-1)][direction][1]
#     while candy_map[start_row][start_col] == candy_map[next_row][next_col]:
#         size += 1
#         next_row = next_row + [(-1,0), (0,1), (1,0), (0,-1)][direction][0]
#         next_col = next_col + [(-1,0), (0,1), (1,0), (0,-1)][direction][1]
#         if not (0 <= next_row < n and 0 <= next_col < n):
#             break
#     return size

# def find_longest():
#     # get start_row, start_col, direction, size
#     start_row = 0
#     start_col = 0
#     start_dir = 0
#     longest_size = 1    
#     for cur_row in range(n):
#         for cur_col in range(n):
#             for direction, (d_row, d_col) in enumerate([(-1,0), (0,1), (1,0), (0,-1)]):
#                 next_row, next_col = cur_row + d_row, cur_col + d_col
#                 if 0 <= next_row < n and 0 <= next_col < n:
#                     if candy_map[cur_row][cur_col] == candy_map[next_row][next_col]:
#                         size = find_depth(cur_row, cur_col, direction) 
#                         if size > longest_size: 
#                             start_row = cur_row
#                             start_col = cur_col
#                             start_dir = direction
#                             longest_size = size
    
#     print(start_row, start_col, start_dir, longest_size)
    
#     # search for adj candies
#     extendable = False
#     candy_type = candy_map[start_row][start_col]
#     cur_head = tuple()
#     cur_tail = tuple()
#     next_head = tuple()
#     next_tail = tuple()
    
    
#     cur_head = (start_row, start_col)
#     if start_dir == 0:
#         next_head = (start_row + 1, start_col)
#         cur_tail = (start_row - size + 1, start_col)
#         next_tail = (start_row - size, start_col)
#     elif start_dir == 1:
#         next_head = (start_row, start_col - 1)
#         cur_tail = (start_row, start_col + size - 1)
#         next_tail = (start_row, start_col + size)
#     elif start_dir == 2:
#         next_head = (start_row - 1, start_col)
#         cur_tail = (start_row + size - 1, start_col)
#         next_tail = (start_row + size, start_col)
#     elif start_dir == 3:
#         next_head = (start_row, start_col + 1)
#         cur_tail = (start_row, start_col - size + 1)
#         next_tail = (start_row, start_col - size)
    
#     for d_r, d_c in [(0,1), (1,0), (0,-1), (-1,0)]:
#         nnh_r = next_head[0] + d_r
#         nnh_c = next_head[1] + d_c
#         if 0 <= next_head[0] < n and 0 <= next_head[1] < n:
#             if 0 <= nnh_r < n and 0 <= nnh_c < n:
#                 if nnh_r == cur_head[0] and nnh_c == cur_head[1]: 
#                     continue
#                 if candy_map[nnh_r][nnh_c] == candy_type: extendable = True
#     if extendable:
#         print(longest_size + 1)
#         return
#     for d_r, d_c in [(0,1), (1,0), (0,-1), (-1,0)]:
#         nnt_r = next_tail[0] + d_r
#         nnt_c = next_tail[1] + d_c
#         if 0 <= next_tail[0] < n and 0 <= next_tail[1] < n:
#             if 0 <= nnt_r < n and 0 <= nnt_c < n:
#                 if nnt_r == cur_tail[0] and nnt_c == cur_tail[1]: 
#                     continue
#                 if candy_map[nnt_r][nnt_c] == candy_type: extendable = True
#     if extendable:
#         print(longest_size + 1)
#         return
#     else:
#         print(longest_size)                      
        
# find_longest()