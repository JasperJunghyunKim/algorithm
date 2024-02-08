########################################
# 23-12-17
# SET

n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]	
# n = 4
# wires = [[1,2],[2,3],[3,4]]	
# n = 7
# wires = [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]	

def solution(n, wires):
    answer = 200
    for i in range(n):
        group_a = []
        group_b = []
        for connection in wires[:i]:
            group_a.extend(connection)
        for connection in wires[i:]:
            group_b.extend(connection)
        print(group_a)
        print(group_b)
        answer = min(answer, abs(len(set(group_a)) - len(set(group_b))))
        
    return answer

print(solution(n, wires))

########################################
# 23-12-15
# BFS 
from collections import deque

# n = 9
# wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]	
# n = 4
# wires = [[1,2],[2,3],[3,4]]	
n = 7
wires = [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]	

def solution(n, wires):
    answer = []

    def bfs(vertex):
        to_visit = deque()
        to_visit.append(vertex)
        visited[vertex] = True
        cnt = 1
        while to_visit:
            cur_v = to_visit.popleft()
            for next_v in range(1, n + 1):
                if graph[cur_v][next_v] == 1 and visited[next_v] == False:
                    to_visit.append(next_v)
                    visited[next_v] = True
                    cnt += 1
        return cnt

    for connection in wires:
        separated = wires[::]
        separated.remove(connection)
        graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
        visited = [False for _ in range(n+1)]
        for v1, v2 in separated:
            graph[v1][v2] = 1
            graph[v2][v1] = 1
        size = []
        for vertex in range(1, n+1):
            if visited[vertex] == False:
                # bfs(vertex, graph, visited)
                size.append(bfs(vertex))
        answer.append(abs(size[0]-size[1]))

    return min(answer)

print(solution(n, wires))