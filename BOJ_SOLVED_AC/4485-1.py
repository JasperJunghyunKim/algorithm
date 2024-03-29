#
# 
#
import sys
sys_input = sys.stdin.readline
import heapq

def dijkstra(start_r, start_c, N):
    shortest_distance = [[float('inf') for _ in range(N)] for _ in range(N)]
    shortest_distance[start_r][start_c] = cave_map[start_r][start_c]
    pq = [(cave_map[start_r][start_c], start_r, start_c)]
    
    while pq:
        min_distance, min_row, min_col = heapq.heappop(pq)
        if shortest_distance[min_row][min_col] < min_distance:
            continue
        else:
            for d_r, d_c in [(0,1), (1,0), (-1,0), (0,-1)]:
                next_r, next_c = min_row + d_r, min_col + d_c
                if 0 <= next_r < N and 0 <= next_c < N and shortest_distance[next_r][next_c] > shortest_distance[min_row][min_col] + cave_map[next_r][next_c]:
                    shortest_distance[next_r][next_c] = shortest_distance[min_row][min_col] + cave_map[next_r][next_c]
                    heapq.heappush(pq, (shortest_distance[min_row][min_col] + cave_map[next_r][next_c], next_r, next_c))
    
    return shortest_distance[N-1][N-1]

p = 1
while True:
    N = int(sys_input())
    if N == 0: 
        break
    cave_map = [list(map(int, sys_input().split())) for _ in range(N)]
    print("Problem " + str(p) + ": " + str(dijkstra(0,0,N)))
    p += 1
    
    
    
