# Index Error 유도한 코드

import sys
sys_input = sys.stdin.readline
N = int(sys_input().strip())
trees = [list(map(int, sys_input().strip().split())) for _ in range(N)]
partial_sum_r_c = [[0] * N for _ in range(N)]

# row1, col1 초기화
partial_sum_r_c[0][0] = trees[0][0]
for r in range(1, N):
    partial_sum_r_c[r][0] = partial_sum_r_c[r-1][0] + trees[r][0]
for c in range(1, N):
    partial_sum_r_c[0][c] = partial_sum_r_c[0][c-1] + trees[0][c]
# row2 ~, col2 ~ 초기화
for r in range(1, N):
    for c in range(1, N):
        partial_sum_r_c[r][c] = trees[r][c] + (partial_sum_r_c[r-1][c] + partial_sum_r_c[r][c-1] - partial_sum_r_c[r-1][c-1])
# print(*partial_sum_r_c, sep="\n")
def find_square_sum(r, c, size):
    if r == 0 and c == 0:
        return partial_sum_r_c[r + size - 1][c + size - 1]
    elif r == 0 and c != 0:
        return partial_sum_r_c[r + size - 1][c + size - 1] - partial_sum_r_c[r + size - 1][c - 1]
    elif r != 0 and c == 0:
        return partial_sum_r_c[r + size - 1][c + size - 1] - partial_sum_r_c[r - 1][c + size - 1]
    else:
        return partial_sum_r_c[r + size - 1][c + size - 1] + partial_sum_r_c[r - 1][c - 1] - partial_sum_r_c[r - 1][c + size - 1] - partial_sum_r_c[r + size - 1][c - 1]

    # 범위 지정을 안해서 Index Error 발생해야되는데, 에러 없이 이상한 값이 출력됨
    # return partial_sum_r_c[r + size - 1][c + size - 1] + partial_sum_r_c[r - 1][c - 1] - partial_sum_r_c[r - 1][c + size - 1] - partial_sum_r_c[r + size - 1][c - 1]


max_profit = -float('inf')
for size in range(1, N + 1):
    for r in range(N - size + 1):
        for c in range(N - size + 1):
            max_profit = max(max_profit,  find_square_sum(r, c, size))

print(max_profit)