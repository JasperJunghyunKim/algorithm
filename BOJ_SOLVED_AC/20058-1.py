import sys
sys_input = sys.stdin.readline
from collections import deque

N, Q = map(int, sys_input().strip().split())
ice_map = [list(map(int, sys_input().strip().split())) for _ in range(2 ** N)]
firestorm = list(map(int, sys_input().strip().split()))

def rotate_clockwise(l):
    subsize = 2**l
    multiple_n = int((2**N) / subsize)
    # 1X1 크기로 나누는 경우엔 제자리므로 회전 불필요
    if l == 0: return
    # 
    for i in range(multiple_n):
        for j in range(multiple_n):
            # 각 부분 조각마다 회전시킴
            rotated_subsquare = []
            cur_r = i * (subsize)
            cur_c = j * (subsize)
            for c in range(cur_c, cur_c + subsize):
                tmp = []
                for r in range(cur_r + subsize - 1, cur_r - 1, -1):
                    tmp.append(ice_map[r][c])
                rotated_subsquare.append(tmp)
            for r in range(subsize):
                for c in range(subsize):
                    ice_map[cur_r + r][cur_c + c] = rotated_subsquare[r][c]
    
def melt_ice():
    d_ice = [[0 for _ in range(2**N)] for _ in range(2**N)]
    for cur_r in range(2**N):
        for cur_c in range(2**N):
            if ice_map[cur_r][cur_c] == 0: continue
            num_adj_ice = 0
            for d_r, d_c in [(0,1), (0,-1), (-1,0), (1,0)]:
                next_r, next_c = cur_r + d_r, cur_c + d_c
                if 0 <= next_r < 2**N and 0 <= next_c < 2**N:
                    if ice_map[next_r][next_c] > 0:
                        num_adj_ice += 1
            # 인접한 얼음의 수가 2 이하면, 해당 얼음은 1 녹음
            if num_adj_ice <= 2:
                d_ice[cur_r][cur_c] = -1

    # 각 칸에 대하여 d_ice 만큼 녹임 
    for r in range(2**N):
        for c in range(2**N):
            ice_map[r][c] += d_ice[r][c]

def bfs():
    visited = [[False for _ in range(2 ** N)] for _ in range(2 ** N)]
    size_ice = [0]
    for r in range(2 ** N):
        for c in range(2 ** N):
            # 얼음이며, not visited
            size = 0
            if ice_map[r][c] >= 1 and not visited[r][c]:
                to_visit = deque([(r,c)])
                visited[r][c] = True
                size += 1
                while to_visit:
                    cur_r, cur_c = to_visit.popleft()
                    for d_r, d_c in [(0,1), (0,-1), (1,0), (-1,0)]:
                        next_r, next_c = cur_r + d_r, cur_c + d_c
                        if 0 <= next_r < 2 ** N and 0 <= next_c < 2 ** N:
                            if ice_map[next_r][next_c] >= 1 and not visited[next_r][next_c]:
                                to_visit.append((next_r, next_c))
                                visited[next_r][next_c] = True
                                size += 1
                size_ice.append(size)
    return max(size_ice)


for l in firestorm:
    rotate_clockwise(l)
    melt_ice()

print(sum([sum(i) for i in ice_map]))
print(bfs())

    