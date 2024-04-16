#
# 24-03-20
# 노드 간 연관 관계를 행렬로 구현할 것이냐, 인접리스트로 구현할 것이냐가 핵심이었음
#


from collections import deque

def solution(n, edge):

    connections = {i:[] for i in range(1, n + 1)}
    for from_v, to_v in edge:
        connections[from_v].append(to_v)
        connections[to_v].append(from_v)
        
    visited = [-1 for _ in range(n + 1)]
    visited[1] = 0
    to_visit = deque()
    to_visit.append(1)
    
    while to_visit:
        cur_v = to_visit.popleft()
        for next_v in connections[cur_v]:
            if visited[next_v] == -1:
                visited[next_v] = visited[cur_v] + 1
                to_visit.append(next_v)
    
    return visited.count(max(visited))