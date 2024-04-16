import sys
sys_input = sys.stdin.readline

num_booze, num_drawer = map(int, sys_input().strip().split())
root = [i for i in range(num_drawer + 1)]
capacity = [1 for _ in range(num_drawer + 1)]
booze_filled = [0 for _ in range(num_drawer + 1)]
depth = [0 for _ in range(num_drawer + 1)]

def find(n):
    if root[n] == n:
        return n
    root[n] = find(root[n])
    return root[n]

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a == root_b: return
    if depth[root_a] > depth[root_b]:
        root[root_b] = root_a
        capacity[root_a] += capacity[root_b]
        booze_filled[root_a] += booze_filled[root_b]
    elif depth[root_a] < depth[root_b]:
        root[root_a] = root_b
        capacity[root_b] += capacity[root_a]
        booze_filled[root_b] += booze_filled[root_a]
    else:
        root[root_b] = root_a
        capacity[root_a] += capacity[root_b]
        booze_filled[root_a] += booze_filled[root_b]
        depth[root_a] += 1
    
for i in range(1, num_booze + 1):
    d_1, d_2 = map(int, sys_input().strip().split())
    union(d_1, d_2)
    if capacity[find(d_1)] > booze_filled[find(d_1)]:
        print("LADICA")
        booze_filled[find(d_1)] += 1
    else:
        print("SMECE")