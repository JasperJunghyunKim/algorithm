########################################
# 23-12-14 (2)
# 시간초과, 메모리초과
# Me 를 기준으로 키큰, 키작은 리스트를 dict 으로 처리 시도

import sys
from collections import deque
sys_input = sys.stdin.readline
num_students, num_comparison = map(int, sys_input().split(' '))
comparison = {i:{1: [], 2:[]} for i in range(1, num_students+1)}
for _ in range(num_comparison):
    a, b = map(int, sys_input().split(' '))
    comparison[a][2].append(b)
    comparison[b][1].append(a)

def num_taller(me):
    taller_list = []
    to_visit = deque()
    taller_list.extend(comparison[me][1])
    to_visit.extend(comparison[me][1])
    while to_visit:
        next_taller = to_visit.popleft()
        taller_list.extend(comparison[next_taller][1])
        taller_list = list(set(taller_list))
        to_visit.extend(comparison[next_taller][1])
    return len(set(taller_list))

def num_shorter(me):
    shorter_list = []
    to_visit = deque()
    shorter_list.extend(comparison[me][2])
    to_visit.extend(comparison[me][2])
    while to_visit:
        next_taller = to_visit.popleft()
        shorter_list.extend(comparison[next_taller][2])
        shorter_list = list(set(shorter_list))
        to_visit.extend(comparison[next_taller][2])
    return len(set(shorter_list))

cnt = 0
for i in range(1, num_students + 1):
    if num_taller(i) + num_shorter(i) == num_students -1:
        cnt += 1
print(cnt)
    

########################################
# 23-12-14 (1)
# 시간초과

import sys
from collections import deque
sys_input = sys.stdin.readline

num_students, num_comparison = map(int, sys_input().split(' '))
taller = [[0 for _ in range(num_students+1)] for _ in range(num_students+1)]
shorter = [[0 for _ in range(num_students+1)] for _ in range(num_students+1)]
num_taller = [0 for _ in range(num_students+1)]
num_shorter = [0 for _ in range(num_students+1)]
for _ in range(num_comparison):
    a, b = map(int, sys_input().split(' '))
    taller[a][b] = 1
    shorter[b][a] = 1

def bfs(start, graph):
    visited = []
    to_visit = deque()
    visited.append(start)
    to_visit.append(start)
    while to_visit:
        cur_student = to_visit.popleft()
        for next_student in range(1, num_students + 1):
            if graph[cur_student][next_student] == 1 and next_student not in visited:
                visited.append(next_student)
                to_visit.append(next_student)
    return len(visited) - 1

# bfs taller, bfs shorter
cnt = 0
for i in range(1, num_students + 1):
    num_taller[i] = bfs(i, taller)
    num_shorter[i] = bfs(i, shorter)
    if num_taller[i] + num_shorter[i] + 1 == num_students:
        cnt+=1
print(cnt)