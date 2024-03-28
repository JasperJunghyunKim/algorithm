#
# 24-03-27
# DFS 와 같은 로직
# 단, PRE, IN, POST 에 따라 visited 체크하는 시점이 다름
# https://m.blog.naver.com/rlakk11/60159303809
#

import sys
sys_input = sys.stdin.readline
tree = {}

NUM_NODE = int(sys_input().strip())
LEFT = 0
RIGHT = 1
for _ in range(NUM_NODE):
    tmp = list(sys_input().strip().split())
    tree[tmp[0]] = []
    tree[tmp[0]].append(tmp[1])
    tree[tmp[0]].append(tmp[2])
        
# PRE ORDER
pre_visited = []
def pre_order(cur_node):
    if cur_node == '.':
        return
    pre_visited.append(cur_node)
    pre_order(tree[cur_node][LEFT])
    pre_order(tree[cur_node][RIGHT])
    
pre_order('A') 
print(*pre_visited, sep='')

# IN ORDER
in_visited = []
def in_order(cur_node):
    if cur_node == '.':
        return
    in_order(tree[cur_node][LEFT])
    in_visited.append(cur_node)
    in_order(tree[cur_node][RIGHT])


in_order('A')
print(*in_visited, sep='')

# POST ORDER
post_visited = []
def post_order(cur_node):
    if cur_node == '.':
        return
    post_order(tree[cur_node][LEFT])
    post_order(tree[cur_node][RIGHT])
    post_visited.append(cur_node)

post_order('A')
print(*post_visited, sep='')
