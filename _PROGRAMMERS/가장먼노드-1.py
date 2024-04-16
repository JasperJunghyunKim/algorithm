#
# 24-03-20 T2
# DIJKSTRA 시간초과
# 가중치 1 이므로, 오히려 성능이 떨어진다
#
def solution(n, edge):
    
    INF = float('infinity')
    distances = [INF] * (n + 1)
    distances[1] = 0
    is_visited = []
    graph = [[] for _ in range(n + 1)]
    
    for from_v, to_v in edge:
        graph[from_v].append(to_v)
        graph[to_v].append(from_v)
    
    while len(is_visited) < n:
        cur_v = None
        cur_min_distance = INF
        
        for node in range(1, n + 1):
            if node not in is_visited and distances[node] < cur_min_distance:
                cur_v = node
                cur_min_distance = distances[node]
        
        for adjacent in graph[cur_v]:
            distances[adjacent] = cur_min_distance + 1 if cur_min_distance + 1 < distances[adjacent] else distances[adjacent]

        is_visited.append(cur_v)

    distances = distances[1:]
    max_distance = max(distances)
    max_cnt = 0
    for d in distances:
        if d == max_distance: max_cnt += 1 
    return max_cnt
    
#
# 24-03-20 T1
# BFS 시간초과
# 처음에 그래프를 2차원 배열로 작성해서 시간초과 -> 인접행렬로 변경하면 해결
#
from collections import deque

def solution(n, edge):
    
    # graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    # for x, y in edge:
    #     graph[x][y] = 1
    #     graph[y][x] = 1
        
    graph = {i:[] for i in range(1, n +1)}
    for x, y in edge:
        graph[x].append(y)
        graph[y].append(x)
    
    visited = [-1 for _ in range(n + 1)]
    to_visit = deque()
    visited[1] = 0
    to_visit.append(1)
    while to_visit:
        cur_v = to_visit.popleft()
        for next_v in graph[cur_v]:
            # if graph[cur_v][next_v] == 1: 
                if visited[next_v] == -1:
                    visited[next_v] = visited[cur_v] + 1
                    to_visit.append(next_v)

    max_distance = max(visited)
    max_cnt = 0
    for distance in visited:
        if distance == max_distance:
            max_cnt += 1

    return max_cnt

if __name__ == "__main__":
    n = 6
    edges = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	
    result = solution(6, edges)
    print(result)