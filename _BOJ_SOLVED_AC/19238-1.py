import sys
sys_input = sys.stdin.readline
from collections import deque
SIZE, NUM_PASSENGER, INIT_FUEL = map(int, sys_input().strip().split())

town = [list(map(int, sys_input().strip().split())) for _ in range(SIZE)]
INIT_TAXI_R, INIT_TAXI_C = map(lambda x : x - 1, map(int, sys_input().strip().split()))
WALL = 1

passenger = dict()
for _ in range(NUM_PASSENGER):
    from_r, from_c, to_r, to_c = map(lambda x : x - 1, map(int, sys_input().strip().split()))
    passenger[(from_r, from_c)] = (to_r, to_c)
    
    
# return distance, passenger_r, passenger_c
def find_closest_passenger(taxi_r, taxi_c):
    
    min_d = float('inf')
    min_r = float('inf')
    min_c = float('inf')
    
    # 택시위치에 승객이 서있으면 바로 리턴
    if (taxi_r, taxi_c) in passenger:
        return (0, taxi_r, taxi_c)
    
    # 택시에서 제일 가까운 승객을 찾음
    visited = [[False for _ in range(SIZE)] for _ in range(SIZE)]
    visited[taxi_r][taxi_c] = True
    to_visit = deque([(taxi_r, taxi_c, 0)])
    while to_visit:
        cur_r, cur_c, cur_d = to_visit.popleft()
        if cur_d > min_d:
            continue
        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            next_r, next_c = cur_r + dr, cur_c + dc
            # 범위 내
            # 벽이 아니고
            if 0 <= next_r < SIZE and 0 <= next_c < SIZE:
                if town[next_r][next_c] != WALL:
                    # 최단거리 승객을 찾으면, 승객 정보를 갱신
                    if (next_r, next_c) in passenger:
                        if cur_d + 1 < min_d:
                            min_d, min_r, min_c = cur_d + 1, next_r, next_c
                        elif cur_d + 1 == min_d:
                            if next_r < min_r:
                                min_r, min_c = next_r, next_c
                            elif next_r == min_r:
                                if next_c < min_c:
                                    min_c = next_c
                    # 그냥 빈칸이라면, min_d 보다 작은 경우에만 append
                    elif visited[next_r][next_c] == False:
                        if cur_d + 1 <= min_d:
                            visited[next_r][next_c] = True
                            to_visit.append((next_r, next_c, cur_d + 1))
                            
    return (min_d, min_r, min_c)

def find_shortest_distance(from_r, from_c, to_r, to_c):
    visited = [[False for _ in range(SIZE)] for _ in range(SIZE)]
    visited[from_r][from_c] = True
    to_visit = deque([(from_r, from_c, 0)])
    while to_visit:
        cur_r, cur_c, cur_d = to_visit.popleft()
        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            next_r, next_c = cur_r + dr, cur_c + dc
            # 목적지를 찾으면 바로 리턴 (그 이후 BFS 실행 불필요)
            if next_r == to_r and next_c == to_c:
                return cur_d + 1
            # 범위 내
            # 벽이 아니고
            # 방문하지 않았으면
            if 0 <= next_r < SIZE and 0 <= next_c < SIZE:
                if town[next_r][next_c] != WALL:
                    if visited[next_r][next_c] == False:
                        visited[next_r][next_c] = True
                        to_visit.append((next_r, next_c, cur_d + 1))
                        
    return float('inf')
    
def drop_passenger(r, c):
    passenger.pop((r, c))

taxi_r, taxi_c = INIT_TAXI_R, INIT_TAXI_C
fuel = INIT_FUEL
for _ in range(NUM_PASSENGER):

    
    # 승객에게 이동
    d, passenger_r, passenger_c = find_closest_passenger(taxi_r, taxi_c)
    if d == float('inf'):
        print(-1)
        exit()
    taxi_r, taxi_c = passenger_r, passenger_c
    fuel -= d
    # print("TO PASSENGER")
    # print("passenger", passenger_r, passenger_c)
    # print("distance", d)
    # print("fuel", fuel)
    # 기름이 없다면 운행 실패
    if fuel < 0: 
        print(-1)
        exit()

    
    # 목적지로 이동
    destination_r, destination_c = passenger[(passenger_r, passenger_c)]
    d = find_shortest_distance(passenger_r, passenger_c, destination_r, destination_c)
    if d == float('inf'):
        print(-1)
        exit()
    taxi_r, taxi_c = destination_r, destination_c
    fuel -= d
    # print("TO DEST")
    # print("destination", passenger_r, passenger_c)
    # print("distance", d)
    # print("fuel", fuel)
    if fuel < 0:
        print(-1)
        exit()
    else:
        fuel += d * 2
    # drop
    drop_passenger(passenger_r, passenger_c)
    # print("DROP")
    # print("passenger list", passenger)


    # 다 내렷으면 
    if len(passenger) == 0:
        break

print(fuel)
    
    