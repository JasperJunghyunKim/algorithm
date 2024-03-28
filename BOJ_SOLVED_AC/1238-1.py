import sys
from collections import deque
sys_input = sys.stdin.readline

NUM_VILLES, NUM_ROADS, PARTY_VILLE = map(int, sys_input().strip().split())
graph = [[0 for _ in range(NUM_VILLES + 1)] for _ in range(NUM_VILLES + 1)]
answer = None

for _ in range(NUM_ROADS):
    from_v, to_v, time = map(int, sys_input().strip().split())
    graph[from_v][to_v] = time

def dijkstra(start_v):
    shortest = [float('INF') for _ in range(NUM_VILLES + 1)]
    shortest[start_v] = 0
    
    to_visit = deque([start_v])
    while to_visit:
        cur_v = to_visit.popleft()
        for next_v in range(1, NUM_VILLES + 1):
            if graph[cur_v][next_v] and shortest[cur_v] + graph[cur_v][next_v] < shortest[next_v]:
                shortest[next_v] = shortest[cur_v] + graph[cur_v][next_v]
                to_visit.append(next_v)

    return shortest

# from PARTY_VILLE to REST
answer = dijkstra(PARTY_VILLE)

# from each ville to PARTY_VILLE
for i in range(1, NUM_VILLES + 1):
    answer[i] += dijkstra(i)[PARTY_VILLE]
    
# 
answer = answer[1:]
print(max(answer))
    