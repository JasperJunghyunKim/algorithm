#
# 24-03-29
# Linear Approach
#
import sys
sys_input = sys.stdin.readline

NUM_V, NUM_E = map(int, sys_input().split())
START_V = int(sys_input())

adj_list = [[] for _ in range(NUM_V + 1)]
for _ in range(NUM_E):
    v_from, v_to, weight = map(int, sys_input().split())
    adj_list[v_from].append((v_to, weight))

def dijkstra(start_node, num_nodes):
    shortest_distance = [float('inf') for _ in range(num_nodes + 1)]
    shortest_distance[start_node] = 0
    visited = [False for _ in range(num_nodes + 1)]
    
    for _ in range(num_nodes):
        min_distance = float('inf')
        min_node = 0
        
        for next_node in range(1, NUM_V + 1):
            if not visited[next_node] and shortest_distance[next_node] < min_distance:
                min_distance = shortest_distance[next_node]
                min_node = next_node
        
        visited[min_node] = True
        
        for adj_node, weight in adj_list[min_node]:
            if shortest_distance[adj_node] > shortest_distance[min_node] + weight:
                shortest_distance[adj_node] = shortest_distance[min_node] + weight
    
    return shortest_distance

shortest_distance = dijkstra(START_V, NUM_V)
for i in range(1, NUM_V + 1):
    print(shortest_distance[i] if shortest_distance[i] != float('inf') else 'INF')
    
#
# Priority Queue
#
import heapq
def dijkstra(start_node, num_nodes):
    shortest_distance = [float('inf') for _ in range(num_nodes + 1)]
    shortest_distance[start_node] = 0
    
    pq = [(0, start_node)]
    while pq:
        min_distance, min_node = heapq.heappop(pq)
        if min_distance > shortest_distance[min_node]:
            continue
        else:
            for adj_node, weight in adj_list[min_node]:
                if shortest_distance[adj_node] > shortest_distance[min_node] + weight:
                    shortest_distance[adj_node] = shortest_distance[min_node] + weight
                    heapq.heappush(pq, (shortest_distance[min_node] + weight, adj_node))
    
    return shortest_distance

shortest_distance = dijkstra(START_V, NUM_V)
for i in range(1, NUM_V + 1):
    print(shortest_distance[i] if shortest_distance[i] != float('inf') else 'INF')