#
# 24-04-10
# 2차원 배열로 푼 것은 9663-4 참조
# 2차원 배열에서는 board(2차원), col(1차원) 배열을 사용하여 이전 Row 에 배치된 Queen 의 위치와 COL 선점 여부를 확인함
# 그러나 queen[c] = r 인 1차원 배열만으로 이를 대체할 수 있음
# 그리고 1차원 배열을 사용해야, r, c 가 유망한지 ,즉, pruning 할 때 시간복잡도를 확 줄일 수 있음
#
# 또한 유망성(promising)을 판단하기 위해
# Backtracking 함수를 Row by Row 로 실행하였고(따라서 Row 는 중복될 수 없음),
# queen[c] >= 0 인 경우 칼럼 중복 여부를 확인 가능
# 대각선은 좌상, 우상만 확인하면 되는데, 2차원보단 오히려 1차원이 더 조건을 정의하기 수월함
#

import sys
N = int(sys.stdin.readline().strip())

num_available = 0
queen = [-1 for _ in range(N)]

def backtrack(r):
    global num_available
    if r == N:
        num_available += 1
        return
    for c in range(N):
        # COL 중복 제거
        if queen[c] >= 0: continue
        # 대각선 중복 제거
        for dc in range(N):
            # dr = queen[dc]
            if queen[dc] == -1: continue
            if queen[dc] + dc == r + c: 
                break
            if queen[dc] - dc == r - c: 
                break
        else:
            queen[c] = r
            backtrack(r + 1)
            queen[c] = -1

backtrack(0)
print(num_available)