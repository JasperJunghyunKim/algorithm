import sys
import heapq
sys_input = sys.stdin.readline

NUM_V, NUM_E = map(int, sys_input().strip().split())
START_V = int(sys_input().strip())
adj_list = [[] for _ in range(NUM_V + 1)]
for _ in range(NUM_E):
    f, t, w = map(int, sys_input().strip().split())
    adj_list[f].append((t,w))

def dijk(start, n):
    dist = [float('inf') for _ in range(n + 1)]
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        d, v = heapq.heappop(pq)
        
        if dist[v] > d:
            continue
        else:
            for adj_v, weight in adj_list[v]:
                if dist[adj_v] > dist[v] + weight:
                    dist[adj_v] = dist[v] + weight
                    heapq.heappush(pq, (dist[v] + weight, adj_v))
    return dist

shortest = dijk(START_V, NUM_V)
for i in range(1, NUM_V + 1):
    if shortest[i] == float('inf'):
        print("INF")
    else:
        print(shortest[i])
    
    