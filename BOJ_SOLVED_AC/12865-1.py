#
# 24-03-16
# 시간초과
#

import sys
sys_input = sys.stdin.readline

num_items, weight_limit = map(int, sys_input().split())
items = [tuple(map(int, sys_input().split())) for _ in range(num_items)]
items.sort(key = lambda x: (x[1]), reverse = True)

def recursive(cur_item_index, total_weight, total_value):
    cur_weight = items[cur_item_index][0]
    cur_value = items[cur_item_index][1]
    
    # Base Condition
    if cur_item_index == num_items - 1:
        if cur_weight <= weight_limit - total_weight:
            total_value += cur_value
        return total_value
    
    # N
    select_n = total_value
    for next_item in range(cur_item_index + 1, num_items):
        next_weight = items[next_item][0]
        if next_weight <= weight_limit - total_weight:
            select_n = recursive(next_item, total_weight, total_value)
            break
    
    # Y
    total_weight += cur_weight
    total_value += cur_value
    select_y = total_value
    for next_item in range(cur_item_index + 1, num_items):
        next_weight = items[next_item][0]
        if next_weight <= weight_limit - total_weight:
            select_y = recursive(next_item, total_weight, total_value)
            break
    
    # compare Y, N
    return max(select_n, select_y)

for item_index, (weight, value) in enumerate(items):
    if weight <= weight_limit:
        print(recursive(item_index, 0, 0))
        break