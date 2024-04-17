import sys
sys_input = sys.stdin.readline

NUM_LAN_TO_CUT, NUM_LAN_NEEDED = map(int, sys_input().strip().split())
cables = [int(sys_input().strip()) for _ in range(NUM_LAN_TO_CUT)]
LEN_MAX = max(cables)

def binary_cut(low, high):
    while low <= high:
        len_to_cut = (low + high) // 2
        num_cables_after_cut = 0
        for cable in cables:
            num_cables_after_cut += (cable // len_to_cut)
        if NUM_LAN_NEEDED <= num_cables_after_cut:
            low = len_to_cut + 1
        elif NUM_LAN_NEEDED > num_cables_after_cut:
            high = len_to_cut - 1
    return high

print(binary_cut(1, LEN_MAX))