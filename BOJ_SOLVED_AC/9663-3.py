#
# 24-04-10
# 1차원 배열로 푼 것은 9663-4 참조
# (참고 : 1차원 배열로 풀어야 시간복잡도를 확 줄일 수 있음)
#

import sys
N = int(sys.stdin.readline().strip())
num_available = 0

board = [[False for _ in range(N)] for _ in range(N)]
col = [False for _ in range(N)]
def backtrack(r):
    global num_available
    if r == N:
        num_available += 1
        return
    # 백트래킹은 Row By Row 로 진행하므로,
    # COL 기준으로만 순회하면 됨
    for c in range(N):
        # 현재 COL 에 Queen 이 있다면 스킵
        if col[c] == True: continue
        # 대각선 좌상, 우상에 Queen 이 있다면 스킵
        # 좌하, 우하는 배치 전이므로 확인할 필요 없음
        # s, e 는 ROW 에 대해 index error 를 방지하기 위해 범위를 좁힌 것
        do_skip = False
        s = c - r if c - r >= 0 else 0
        for dc in range(s, c):
            if board[dc + r - c][dc] == True: do_skip = True
        e = c + r + 1 if c + r + 1 <= N else N
        for dc in range(c + 1, e):
            if board[r + c - dc][dc] == True: do_skip = True
        if do_skip:
            continue
        board[r][c] = True
        col[c] = True
        backtrack(r + 1)
        board[r][c] = False
        col[c] = False

backtrack(0)
print(num_available)