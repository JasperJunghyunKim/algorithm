#
# 24-03-29 - Linear Approach
#
import sys
sys_input = sys.stdin.readline

NUM_V, NUM_E = map(int, sys_input().split(' '))
START_V = int(sys_input())

graph = [[] for _ in range(NUM_V + 1)]

for _ in range(NUM_E):
    v_from, v_to, w = map(int, sys_input().split(' '))
    graph[v_from].append((v_to, w))
                
def dijkstra(START_V):
    global NUM_V
    shortest_path = [float('inf') for _ in range(NUM_V + 1)]
    shortest_path[START_V] = 0
    visited = [False] * (NUM_V + 1)

    for _ in range(NUM_V):
        min_distance = float('inf')
        min_v = 0
        
        for v in range(1, NUM_V + 1):
            if not visited[v] and shortest_path[v] < min_distance:
                min_distance = shortest_path[v]
                min_v = v
        
        visited[min_v] = True
        
        for next_v, w in graph[min_v]:
            if shortest_path[next_v] > shortest_path[min_v] + w:
                shortest_path[next_v] = shortest_path[min_v] + w
        
    return shortest_path

shortest_path = dijkstra(START_V)

for i in range(1, NUM_V + 1):
    if shortest_path[i] == float('inf'):
        print("INF")
        continue
    print(shortest_path[i])