# 1. 루트가 여러개
# 2. 루트노드가 리프노드인 경우
import sys
sys_input = sys.stdin.readline
NUM_NODES = int(sys_input().strip())
parent = list(map(int, sys_input().strip().split()))
children = [set() for _ in range(NUM_NODES)]
for node, p in enumerate(parent):
    if p == -1: continue
    children[p].add(node)
NODE_TO_REMOVE = int(sys_input().strip())
p = parent[NODE_TO_REMOVE]
if p != -1:
    children[p].remove(NODE_TO_REMOVE)
num_leaf_node = 0


def count_leaf_nodes(root):
    global num_leaf_node
    to_visit = [root]
    while to_visit:
        cur_v = to_visit.pop()
        if cur_v == NODE_TO_REMOVE: continue
        if not children[cur_v]:
            num_leaf_node += 1
        else:
            to_visit.extend(children[cur_v])

for node, p in enumerate(parent):
    if p == -1:
        count_leaf_nodes(node)
print(num_leaf_node)
