#
# 24-03-16
# 노가다로 해결
#

import sys
sys_input = sys.stdin.readline

# 4 ~ 500
num_rows, num_cols = map(int, sys_input().split())

number_map = []
for _ in range(num_rows):
    number_map.append(list(map(int, sys_input().split())))

#
three_by_two = [
    [(0,0), (1,0), (2,0), (0,1)],
    [(0,0), (1,0), (2,0), (1,1)],
    [(0,0), (1,0), (2,0), (2,1)],
    [(0,1), (1,1), (2,1), (0,0)],
    [(0,1), (1,1), (2,1), (1,0)],
    [(0,1), (1,1), (2,1), (2,0)],
    [(0,0), (1,0), (1,1), (2,1)],
    [(1,0), (2,0), (0,1), (1,1)]
]

#
two_by_three = [
    [(0,0), (0,1), (0,2), (1,0)],
    [(0,0), (0,1), (0,2), (1,1)],
    [(0,0), (0,1), (0,2), (1,2)],
    [(1,0), (1,1), (1,2), (0,0)],
    [(1,0), (1,1), (1,2), (0,1)],
    [(1,0), (1,1), (1,2), (0,2)],
    [(0,0), (0,1), (1,1), (1,2)],
    [(1,0), (1,1), (0,1), (0,2)]
]

#
def find_max(size_row, size_col, cur_row, cur_col):
    result = 0
    if size_row == 1 and size_col == 4:
        for i in range(4):
            result += number_map[cur_row][cur_col + i]
    elif size_row == 4 and size_col == 1:
        for i in range(4):
            result += number_map[cur_row + i][cur_col]
    elif size_row == 2 and size_col == 2:
        for i in range(2):
            for j in range(2):
                result += number_map[cur_row + i][cur_col + j]
    elif size_row == 2 and size_col == 3:
        for tetromino in two_by_three:
            tmp = 0
            for d_r, d_c in tetromino:
                tmp += number_map[cur_row + d_r][cur_col + d_c]
            result = tmp if tmp > result else result
    elif size_row == 3 and size_col == 2:
        for tetromino in three_by_two:
            tmp = 0
            for d_r, d_c in tetromino:
                tmp += number_map[cur_row + d_r][cur_col + d_c]
            result = tmp if tmp > result else result
    return result

max_value = 0
# 1 * 4 : 1
for cur_row in range(num_rows):
    for cur_col in range(num_cols - 3):
        tmp = find_max(1, 4, cur_row, cur_col)
        max_value = tmp if tmp > max_value else max_value
                
# 4 * 1 : 1
for cur_row in range(num_rows - 3):
    for cur_col in range(num_cols):
        tmp = find_max(4, 1, cur_row, cur_col)
        max_value = tmp if tmp > max_value else max_value

# 2 * 2 : 1
for cur_row in range(num_rows - 1):
    for cur_col in range(num_cols - 1):
        tmp = find_max(2, 2, cur_row, cur_col)
        max_value = tmp if tmp > max_value else max_value

# 3 * 2 : 8
for cur_row in range(num_rows - 2):
    for cur_col in range(num_cols - 1):
        tmp = find_max(3, 2, cur_row, cur_col)
        max_value = tmp if tmp > max_value else max_value

# 2 * 3 : 8
for cur_row in range(num_rows - 1):
    for cur_col in range(num_cols - 2):
        tmp = find_max(2, 3, cur_row, cur_col)
        max_value = tmp if tmp > max_value else max_value

print(max_value)