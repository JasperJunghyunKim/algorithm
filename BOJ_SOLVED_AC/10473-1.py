import sys
import heapq
import math
sys_input = sys.stdin.readline

START_X, START_Y = map(float, sys_input().split())
END_X, END_Y = map(float, sys_input().split())
NUM_CANNON = int(sys_input())
cannons = []
shortest_time = {(START_X, START_Y): 0, (END_X, END_Y): float('inf')}
for _ in range(NUM_CANNON):
    cannon_x, cannon_y = map(float, sys_input().split())
    shortest_time[(cannon_x, cannon_y)] = float('inf')
    cannons.append((cannon_x, cannon_y))

positions = list(shortest_time.keys())

# cannons
# positions
# shortest_time

def get_time(start_x, start_y, end_x, end_y, start_is_cannon):
    distance = math.sqrt((start_x - end_x)**2 + (start_y - end_y)**2)
    if not start_is_cannon:
        return distance / 5
    else:
        # 50 미터 이상이면 쏘고 + 정방향 뛴다
        if distance >= 50:
            return 2 + (distance - 50) / 5
        
        # 50 미터 미만이면, min(쏘고 + 역방향 뛴다, 정방향 뛴다)
        else:
            return min(2 + (50 - distance) / 5, distance / 5)

def dijkstra(START_X, START_Y):
    pq = [(0, START_X, START_Y)]
    
    while pq:
        min_time, min_x, min_y = heapq.heappop(pq)
        if shortest_time[(min_x, min_y)] < min_time:
            continue
        else:
            for next_x, next_y in positions:
                dt = get_time(min_x, min_y, next_x, next_y, (min_x, min_y) in cannons)
                if shortest_time[(next_x, next_y)] > shortest_time[(min_x, min_y)] + dt:
                    shortest_time[(next_x, next_y)] = shortest_time[(min_x, min_y)] + dt
                    heapq.heappush(pq, (shortest_time[(min_x, min_y)] + dt, next_x, next_y))
    
    return shortest_time

shortest_time = dijkstra(START_X, START_Y)    
print(shortest_time[(END_X, END_Y)])        