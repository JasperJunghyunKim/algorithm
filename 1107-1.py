import sys
sys_input = sys.stdin.readline

target_channel = int(sys_input().strip())
num_not_working = int(sys_input().strip())
working_buttons = set([str(i) for i in range(10)])
min_clicks = float('inf')
if num_not_working > 0:
    working_buttons -= set(sys_input().strip().split())

# 
if target_channel == 100:
    print(0)
    exit()

# 
zero_in_working_buttons = ('0' in working_buttons)
num_clicks_bound_zero = 1 + target_channel

#
for i in range(10):
    channel_above = target_channel + i
    channel_below = target_channel - i
    check_below = True
    if channel_below < 0:
        False
    
    digits_above_issubset = set(str(channel_above)).issubset(working_buttons)
    digits_below_issubset = set(str(channel_above)).issubset(working_buttons)
    num_clicks_above = i + len(str(channel_above))
    num_clicks_below = i + len(str(channel_below))
    
    # print(i)
    # print(zero_in_working_buttons)
    # print(num_clicks_bound_zero)
    # print(check_below)
    # print(digits_above_issubset)
    # print(digits_below_issubset)
    
    
    # 위
    if not channel_below and digits_above_issubset:
        min_clicks = min(min_clicks, num_clicks_above)
        break
    
    # 위 아래   
    elif channel_below and digits_above_issubset and digits_below_issubset:
        min_clicks = min(min_clicks, num_clicks_above, num_clicks_below)
        break

if zero_in_working_buttons:
    min_clicks = min(min_clicks, num_clicks_bound_zero)
print(min_clicks)