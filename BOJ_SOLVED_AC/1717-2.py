#
# 24-03-27
#
n, num_tc = map(int, input().strip().split())
root = [i for i in range(n + 1)]
depth = [0 for _ in range(n + 1)]

# find
def find(n):
    if root[n] == n:
        return n
    root[n] = find(root[n])
    return root[n]

# union
def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a == root_b: 
        return
    if depth[root_a] > depth[root_b]:
        root[root_b] = root_a
    elif depth[root_a] < depth[root_b]:
        root[root_a] = root_b
    else:
        root[root_b] = root_a
        depth[root_a] += 1

# get result
for _ in range(num_tc):
    cmd, a, b = map(int, input().strip().split())
    if cmd == 0:
        union(a, b)
    elif cmd == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")