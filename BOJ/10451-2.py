#
# 24-03-12
# Visited 관리를 boolean 값으로 적용해서 시간 단축 (3600 ms -> 260 ms)
#

# Trial 1
import sys
sys_input = sys.stdin.readline

num_tc = int(sys_input().strip())
num_v = 0
num_cycles = 0

def dfs(cur_v, visited, sequence):
    visited.append(cur_v)
    next_v = sequence[cur_v]
    if next_v not in visited:
        dfs(next_v, visited, sequence)
    
for _ in range(num_tc):
    num_v = int(sys_input().strip())
    num_cycles = 0
    sequence = [0]
    sequence.extend(list(map(int, sys_input().strip().split())))
    visited = []
    for index, value in enumerate(sequence):
        if index == 0: continue
        if index not in visited:
            num_cycles += 1
            dfs(index, visited, sequence)
    print(num_cycles)

# Trial 2
for _ in range(num_tc):
    num_v = int(sys_input().strip())
    num_cycles = 0
    sequence = [0]
    sequence.extend(list(map(int, sys_input().strip().split())))
    visited = [False] * (num_v + 1)
    for k, v in enumerate(sequence):
        if k == 0: continue
        if not visited[k]:
            num_cycles += 1
            visited[k] = True
            next_v = sequence[k]
            while not visited[next_v]:
                visited[next_v] = True
                next_v = sequence[next_v]
    print(num_cycles)
