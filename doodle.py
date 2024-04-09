import sys
sys_input = sys.stdin.readline

NUM_SETS, NUM_CMD = map(int, sys_input().strip().split())

# Make Set
root = [i for i in range(NUM_SETS + 1)]
depth = [0 for _ in range(NUM_SETS + 1)]

# Union
def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if depth[x] > depth[y]:
        root[y] = x
    elif depth[y] > depth[x]:
        root[x] = y
    else:
        root[x] = y
        depth[y] += 1

# Find
def find(x):
    if x == root[x]:
        return x
    root[x] = find(root[x])
    return root[x]

for _ in range(NUM_CMD):
    cmd, x, y = map(int, sys_input().strip().split())
    if cmd == 0:
        union(x, y)
    elif cmd == 1:
        if find(x) == find(y): print("YES")
        else: print("NO")