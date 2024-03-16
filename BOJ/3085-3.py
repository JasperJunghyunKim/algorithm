#
# 24-03-16
#
import sys
sys_input = sys.stdin.readline

n = int(sys_input().strip())

candy_map = []

for _ in range(n):
    candy_map.append(list(sys_input().strip()))
    
# 
def find_longest():
    longest_size = 1
    
    # row
    for row in range(n):
        temp_size = 1
        for col in range(n):
            if col == n-1 or candy_map[row][col] != candy_map[row][col + 1]:
                longest_size = temp_size if temp_size > longest_size else longest_size
                temp_size = 1
            else:
                temp_size += 1
    
    # col
    for col in range(n):
        temp_size = 1
        for row in range(n):
            if row == n-1 or candy_map[row][col] != candy_map[row + 1][col]:
                longest_size = temp_size if temp_size > longest_size else longest_size
                temp_size = 1
            else:
                temp_size += 1
    
    return longest_size

#
def swap(row_a, col_a, row_b, col_b):
    # tmp = candy_map[row_a][col_a]
    # candy_map[row_a][col_a] = candy_map[row_b][col_b]
    # candy_map[row_b][col_b] = tmp
    candy_map[row_a][col_a], candy_map[row_b][col_b] = candy_map[row_b][col_b], candy_map[row_a][col_a]

longest_size = 1
for cur_row in range(n):
    for cur_col in range(n):
        for d_r, d_c in [(0,1), (1,0)]:
            next_row = cur_row + d_r
            next_col = cur_col + d_c
            if next_row < n and next_col < n:
                swap(cur_row, cur_col, next_row, next_col)
                temp_size = find_longest()
                longest_size = temp_size if temp_size > longest_size else longest_size
                swap(cur_row, cur_col, next_row, next_col)

print(longest_size)