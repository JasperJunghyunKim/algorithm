import sys
sys_input = sys.stdin.readline

HAVE, NEED = map(int, sys_input().strip().split())
lan_cables = [int(sys_input().strip()) for _ in range(HAVE)]
max_length = 0


def binary_cut(min_cut_len, max_cut_len):
    
    while min_cut_len < max_cut_len:
        mid_cut_len = (min_cut_len + max_cut_len) // 2
        cnt = 0
        for cable in lan_cables:
            cnt += cable // mid_cut_len
        if cnt < NEED:
            max_cut_len = mid_cut_len - 1
        else:
            min_cut_len = mid_cut_len + 1
    return min_cut_len - 1
    # if low == high:
    #     return low
    # mid = (low + high) // 2
    # cnt = 0
    # for cable in lan_cables:
    #     cnt += cable // mid
    # if cnt < NEED:
    #     return binary_cut(low, mid - 1)
    # elif cnt >= NEED:
    #     return binary_cut(mid + 1, high)



# if HAVE >= NEED:
#     print(min(lan_cables))
#     exit()
# else:
print(binary_cut(1, max(lan_cables)))