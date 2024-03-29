#
# 24-03-29
# PriorityQueue (단순 접근)
#
import sys
import heapq
sys_input = sys.stdin.readline


NUM_VILLE, NUM_ROAD, PARTY_VILLE = map(int, sys_input().split())
adj_list = [[] for _ in range(NUM_VILLE + 1)]
for _ in range(NUM_ROAD):
    v_from, v_to, time = map(int, sys_input().split())
    adj_list[v_from].append((v_to, time))

def dijkstra(start_ville):
    shortest_time = [float('inf') for _ in range(NUM_VILLE + 1)]
    shortest_time[start_ville] = 0
    pq = [(0, start_ville)]
    
    while pq:
        min_distance, min_ville = heapq.heappop(pq)
        if min_distance > shortest_time[min_ville]:
            continue
        else:
            for adj_ville, time in adj_list[min_ville]:
                if shortest_time[adj_ville] > shortest_time[min_ville] + time:
                    shortest_time[adj_ville] = shortest_time[min_ville] + time
                    heapq.heappush(pq, (shortest_time[min_ville] + time, adj_ville))
    
    return shortest_time

shortest_time = dijkstra(PARTY_VILLE)
for i in range(1, NUM_VILLE + 1):
    shortest_time[i] += dijkstra(i)[PARTY_VILLE]
    
print(max(shortest_time[1::]))

#
# Reverse Dijkstra
# https://chb2005.tistory.com/128
#
import sys
import heapq
sys_input = sys.stdin.readline


NUM_VILLE, NUM_ROAD, PARTY_VILLE = map(int, sys_input().split())
map_normal = [[] for _ in range(NUM_VILLE + 1)]
map_reversed = [[] for _ in range(NUM_VILLE + 1)]
for _ in range(NUM_ROAD):
    v_from, v_to, time = map(int, sys_input().split())
    map_normal[v_from].append((v_to, time))
    map_reversed[v_to].append((v_from, time))
    
def dijkstra(start_node, map):
    shortest_time = [float('inf') for _ in range(NUM_VILLE + 1)]
    shortest_time[start_node] = 0
    dq = [(0, start_node)]
    
    while dq:
        min_distance, min_ville = heapq.heappop(dq)
        if shortest_time[min_ville] < min_distance:
            continue
        else:
            for adj_ville, time in map[min_ville]:
                if shortest_time[adj_ville] > shortest_time[min_ville] + time:
                    shortest_time[adj_ville] = shortest_time[min_ville] + time
                    heapq.heappush(dq, (shortest_time[min_ville] + time, adj_ville))
                    
    return shortest_time

# Party Ville 에서 나머지 Ville 까지 소요되는 시간
shortest_time = dijkstra(PARTY_VILLE, map_normal)

# 나머지 Ville 에서 Party Ville 까지 소요되는 시간 (Reversed Dijkstra)
shortest_time_reversed = dijkstra(PARTY_VILLE, map_reversed)

maxtime = 0
for i in range(1, NUM_VILLE + 1):
    maxtime = max(maxtime, shortest_time[i] + shortest_time_reversed[i])
print(maxtime)