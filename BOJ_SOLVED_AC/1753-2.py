import sys
import heapq
sys_input = sys.stdin.readline

NUM_V, NUM_E = map(int, sys_input().split())
START_V = int(sys_input())

adj_list = [[] for _ in range(NUM_V + 1)]
for _ in range(NUM_E):
    v_from, v_to, weight = map(int, sys_input().split())
    adj_list[v_from].append((v_to, weight))
    
def dijkstra(START_V):
    shortest_path = [float('inf') for _ in range(NUM_V + 1)]
    shortest_path[START_V] = 0

    queue = [(0, START_V)]
    while queue:
        cur_dist, cur_v = heapq.heappop(queue)
        if shortest_path[cur_v] < cur_dist:
            continue
        else:
            for next_v, weight in adj_list[cur_v]:
                if shortest_path[next_v] > shortest_path[cur_v] + weight:
                    shortest_path[next_v] = shortest_path[cur_v] + weight
                    heapq.heappush(queue, (shortest_path[cur_v] + weight, next_v))
                    
    return shortest_path

shortest_path = dijkstra(START_V)
for i in range(1, NUM_V + 1):
    print("INF" if shortest_path[i] == float('inf') else shortest_path[i])
    