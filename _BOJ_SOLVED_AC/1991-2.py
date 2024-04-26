import sys
sys_input = sys.stdin.readline
NUM_NODES = int(sys_input().strip())
PRE, IN, POST = 0, 1, 2
tree = {}
for _ in range(NUM_NODES):
    parent, left, right = sys_input().strip().split()
    tree[parent] = []
    tree[parent].append(left)
    tree[parent].append(right)

def dfs(cur_v, order):
    left_v = tree[cur_v][0]
    right_v = tree[cur_v][1]
    if order == 0:
        print(cur_v, end="")
        if left_v != '.': dfs(left_v, 0)
        if right_v != '.': dfs(right_v, 0)
    elif order == 1:
        if left_v != '.': dfs(left_v, 1)
        print(cur_v, end="")
        if right_v != '.': dfs(right_v, 1)
    elif order == 2:
        if left_v != '.': dfs(left_v, 2)
        if right_v != '.': dfs(right_v, 2)
        print(cur_v, end="")

dfs('A', PRE)
print()
dfs('A', IN)
print()
dfs('A', POST)