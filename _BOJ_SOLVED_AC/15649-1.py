# T2 - itertool permutation
from itertools import permutations
n, len_seq = map(int, input().strip().split(' '))
sequence = list(permutations([i for i in range(1, n+1)], len_seq))
for i in sequence:
    print(*i, sep=' ')

# T1 - DFS 재귀
import copy
n, len_sequence = map(int, input().strip().split(' '))

def dfs(node, visited):
    buffer = copy.deepcopy(visited)
    buffer.append(node)
    if len(buffer) == len_sequence:
        print(*buffer, sep=' ')
    else:
        for i in range(1, n+1):
            if i not in buffer:
                dfs(i, buffer)

for i in range(1, n+1):
    dfs(i, [])