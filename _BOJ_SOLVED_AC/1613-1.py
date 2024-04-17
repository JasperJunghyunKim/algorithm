#
# Floyd Warshall PyPy3 으로 통과
# DFS 왜 틀렸는지 모름...
#

import sys
sys_input = sys.stdin.readline

NUM_EVENTS, NUM_REL = map(int, sys_input().strip().split())

# FLOYD WARSHALL
graph = [[float('inf')] * NUM_EVENTS for _ in range(NUM_EVENTS)]
for _ in range(NUM_REL):
    event_before, event_after = map(int, sys_input().strip().split())
    graph[event_before - 1][event_after - 1] = 1

for e in range(NUM_EVENTS):
    graph[e][e] = 0

for step_over in range(NUM_EVENTS):
    for event_a in range(NUM_EVENTS):
        for event_b in range(NUM_EVENTS):
            graph[event_a][event_b] = min(graph[event_a][event_b], graph[event_a][step_over] + graph[step_over][event_b])

for _ in range(int(sys_input().strip())):
    event_a, event_b = map(int, sys_input().strip().split())
    event_a -= 1
    event_b -= 1
    if graph[event_a][event_b] != float('inf'):
        print(-1)
    elif graph[event_b][event_a] != float('inf'):
        print(1)
    else:
        print(0)


# DFS
# graph = {i: [] for i in range(1, NUM_EVENTS + 1)}
#
# for _ in range(NUM_REL):
#     event_before, event_after = map(int, sys_input().strip().split())
#     graph[event_before].append((event_after))
#
# def a_then_b(event_a, event_b):
#     visited = {event_a:True}
#
#     def recursive(cur_event):
#         if cur_event == event_b:
#             return True
#         for next_event in graph[cur_event]:
#             if next_event not in visited:
#                 visited[next_event] = True
#                 return recursive(next_event)
#         return False
#
#     return recursive(event_a)
#
# NUM_COMPARISON = int(sys_input().strip())
# for _ in range(NUM_COMPARISON):
#     event_a, event_b = map(int, sys_input().strip().split())
#     if a_then_b(event_a, event_b):
#         print(-1)
#     elif a_then_b(event_b, event_a):
#         print(1)
#     else:
#         print(0)