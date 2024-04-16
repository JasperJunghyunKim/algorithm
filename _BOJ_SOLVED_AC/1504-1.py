#
# 24-03-29
# 정점의 수가 적으므로 선형탐색으로 시도
#
import sys
sys_input = sys.stdin.readline

NUM_V, NUM_E = map(int, sys_input().split())
adj_list = [[] for _ in range(NUM_V + 1)]

for _ in range(NUM_E):
    v_from, v_to, weight = map(int, sys_input().split())
    adj_list[v_from].append((v_to, weight))
    adj_list[v_to].append((v_from, weight))
    
REQUIRED_1, REQUIRED_2 = map(int, sys_input().split())

def dijkstra(start_v, end_v, NUM_V):
    shortest_distance = [float('inf') for _ in range(NUM_V + 1)]
    shortest_distance[start_v] = 0
    visited = [False for _ in range(NUM_V + 1)]
    
    for _ in range(NUM_V):
        min_distance = float('inf')
        min_v = 0
        
        for v in range(1, NUM_V + 1):
            if not visited[v] and shortest_distance[v] < min_distance:
                min_distance = shortest_distance[v]
                min_v = v
        
        visited[min_v] = True
        
        for adj_v, weight in adj_list[min_v]:
            if shortest_distance[adj_v] > shortest_distance[min_v] + weight:
                shortest_distance[adj_v] = shortest_distance[min_v] + weight
    
    return shortest_distance[end_v]
    
answer = min(dijkstra(1, REQUIRED_1, NUM_V) + dijkstra(REQUIRED_2, NUM_V, NUM_V) + dijkstra(REQUIRED_1, REQUIRED_2, NUM_V), dijkstra(1, REQUIRED_2, NUM_V) + dijkstra(REQUIRED_1, NUM_V, NUM_V) + dijkstra(REQUIRED_2, REQUIRED_1, NUM_V))

print(answer if answer != float('inf') else -1)


#
# 24-03-29
# PRIORITY QUEUE
#
import sys
import heapq
sys_input = sys.stdin.readline

NUM_V, NUM_E = map(int, sys_input().split())
graph = [[-1 for _ in range(NUM_V + 1)] for _ in range(NUM_V + 1)]

for _ in range(NUM_E):
    v_from, v_to, weight = map(int, sys_input().split())
    graph[v_from][v_to] = weight
    graph[v_to][v_from] = weight
    
REQUIRED_1, REQUIRED_2 = map(int, sys_input().split())

def dijkstra(start_v, NUM_V):
    shortest_distance = [float('inf') for _ in range(NUM_V + 1)]
    shortest_distance[start_v] = 0
    pq = [(0, start_v)]

    while pq:
        min_distance, min_v = heapq.heappop(pq)
        if min_distance > shortest_distance[min_v]:
            continue
        else:
            for next_v in range(1, NUM_V + 1):
                if graph[min_v][next_v] != -1 and shortest_distance[next_v] > shortest_distance[min_v] + graph[min_v][next_v]:
                    shortest_distance[next_v] = shortest_distance[min_v] + graph[min_v][next_v]
                    heapq.heappush(pq, (shortest_distance[min_v] + graph[min_v][next_v], next_v))
    
    return shortest_distance

shortest_1 = dijkstra(1, NUM_V)
shortest_2 = dijkstra(REQUIRED_1, NUM_V)
shortest_3 = dijkstra(REQUIRED_2, NUM_V)
    
answer = min(shortest_1[REQUIRED_1] + shortest_2[REQUIRED_2] + shortest_3[NUM_V], shortest_1[REQUIRED_2] + shortest_3[REQUIRED_1] + shortest_2[NUM_V])

print(answer if answer != float('inf') else -1)