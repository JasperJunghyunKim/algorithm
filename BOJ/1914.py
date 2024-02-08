import sys
from collections import deque
n = int(sys.stdin.readline())

hanoi_start = {
    1:deque([i for i in range(1, n+1)]),
    2:deque(),
    3:deque()
}

hanoi_result = {
    1:deque(),
    2:deque(),
    3:deque([i for i in range(1, n+1)])
}

shortest = []

visited = []

trace = []

def possible_moves(status):
    possible_moves = []
    if status[1][0] < status[2][0]:
        possible_moves.append(1,2)
    if status[1][0] < status[3][0]:
        possible_moves.append(1,3)
    if status[2][0] < status[3][0]:
        possible_moves.append(2,3)
    if status[2][0] < status[1][0]:
        possible_moves.append(2,1)
    if status[3][0] < status[1][0]:
        possible_moves.append(3,1)
    if status[3][0] < status[2][0]:
        possible_moves.append(3,2)
    return possible_moves

def find_next_status(current_status, move):
    current_status[move[1]].appendleft(current_status[move[0]].popleft())
    return current_status

def dfs(status, visited, trace):
    if status == hanoi_result:
        # 결과
        pass
    visited.append(status)
    if 
    for move in possible_moves(status):
        next_status = find_next_status(status, move)
        if next_status in visited:
            continue
        trace.append(move)
        dfs(next_status, visited, trace)
