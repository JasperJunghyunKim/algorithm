import sys
sys_input = sys.stdin.readline
from collections import Counter

NUM_TREES, MIN_METERS_REQUIRED = map(int, sys_input().strip().split())
trees = Counter(map(int, sys_input().strip().split()))
TREE_MAX_HEIGHT = max(trees)

def binary_cut(low, high):
    to_cut = 0
    while low <= high:
        to_cut = (low + high) // 2
        meters_after_cut = 0
        for tree in trees.keys():
            meters_after_cut += (tree - to_cut) * trees[tree] if tree - to_cut > 0 else 0

        # 잘린 길이가 같거나 충분하면, 높이를 늘린다
        if meters_after_cut >= MIN_METERS_REQUIRED:
            low = to_cut + 1

        # 잘린 길이가 부족하면, 높이를 줄인다
        elif meters_after_cut < MIN_METERS_REQUIRED:
            high = to_cut - 1

    # high 를 리턴하는 것 주의
    return high

print(binary_cut(0, TREE_MAX_HEIGHT))