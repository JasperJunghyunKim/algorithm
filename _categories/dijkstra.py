#
# 블로그 글 참고
# https://velog.io/@hyesoup/%EC%9D%B4%EA%B2%83%EC%9D%B4-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%8B%A4-%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
#
# 정리
# 1. 출발 노드 설정
# 2. 최단 거리 테이블 초기화
# 3. 방문하지 않은 노드 중 최단거리가 가장 짧은 노드를 선택
# 4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신
# 5. 3, 4 를 반복
#


INF = float('infinity')

def dijkstra(graph, start_v):
    distances = [INF] * (len(graph) + 1)
    distances[start_v] = 0
    
    is_visited = []
    
    while len(is_visited) < len(graph):
        # 아직 처리하지 않은 정점 중 최단 거리가 가장 짧은 정점 찾기
        cur_v = None
        cur_min_distance = INF
        for vertex in distances:
            if vertex not in is_visited and distances[vertex] < cur_min_distance:
                cur_v = vertex
                cur_min_distance = distances[vertex]
        
        # 찾은 정점을 기준으로 업데이트
        for adjacent, weight in graph[cur_v]:
            distance = cur_min_distance + weight
            if distance < distances[adjacent]:
                distances[adjacent] = distances
        
        is_visited.append(cur_v)
    
    return distances