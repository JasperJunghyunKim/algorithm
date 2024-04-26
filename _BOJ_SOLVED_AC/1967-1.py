# T3
# 이건 일반적으로 트리의 지름을 구하는 방법
# https://johoonday.tistory.com/217 

# T2
# 모든 노드의 좌우 각각의 최대 길이를 찾는다
# 예) 예제의 3번 노드의 좌의 최대 길이는 11 + 15, 우의 최대 길이는 9 + 10
# 모든 노드에 대해, 좌우 합이 최대가 되는 길이가 '지름' 이 됨
import sys
sys.setrecursionlimit(10_010)
sys_input = sys.stdin.readline
NUM_V = int(sys_input().strip())
graph = {i:[] for i in range(1, NUM_V + 1)}
for _ in range(NUM_V - 1):
    v_a, v_b, weight = map(int, sys_input().strip().split())
    graph[v_a].append((v_b, weight))
    # graph[v_b].append((v_a, weight))

weight_tree = {i:[0] for i in range(1, NUM_V + 1)}

def dfs_post_order(parent_v):
    if not graph[parent_v]:
        weight_tree[parent_v].append(0)
        return
    for next_v, weight in graph[parent_v]:
        dfs_post_order(next_v)
    for next_v, weight in graph[parent_v]:
        weight_tree[parent_v].append(weight + max(weight_tree[next_v]))

dfs_post_order(1)

max_radius = 0
for i in weight_tree.values():
    if len(i) >= 2:
        i.sort(reverse=True)
        if i[0] + i[1] > max_radius: max_radius = i[0] + i[1]

print(max_radius)

# T1
# DFS 로 다 탐색하면 O(N) * O(N + E) 이므로, 약 2억번 계산이라서 무조건 시간초과가 난다

# import sys
# sys_input = sys.stdin.readline
# NUM_NODES = int(sys_input().strip())
# graph = {i:[] for i in range(1, NUM_NODES + 1)}
# g_max_distance = 0
# for _ in range(NUM_NODES - 1):
#     node_a, node_b, weight = map(int, sys_input().strip().split())
#     graph[node_a].append((node_b, weight))
#     graph[node_b].append((node_a, weight))
#
#
# def find_longest_distance(start_v):
#     global g_max_distance
#     visited = [False] * (NUM_NODES + 1)
#     visited[start_v] = True
#     to_visit = [(start_v, 0)]
#
#     while to_visit:
#         cur_v, cur_d = to_visit.pop()
#         if cur_d > g_max_distance:
#             g_max_distance = cur_d
#         for next_v, weight in graph[cur_v]:
#             if not visited[next_v]:
#                 visited[next_v] = True
#                 to_visit.append((next_v, cur_d + weight))
#
#
#
# for v in range(1, NUM_NODES + 1):
#     find_longest_distance(v)
#
# print(g_max_distance)

