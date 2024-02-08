from collections import deque

graph = {
    'A' : ['B', 'C'],
    'B' : ['A', 'D'],
    'C' : ['A', 'G', 'H', 'I'],
    'D' : ['B', 'E', 'F'],
    'E' : ['D'],
    'F' : ['D'],
    'G' : ['C'],
    'H' : ['C'],
    'I' : ['C', 'J'],
    'J' : ['I']
}

def bfs(vertex):
    visited = []
    to_visit = deque()
    to_visit.append(vertex)
    while to_visit:
        next_vertex = to_visit.popleft()
        visited.append(next_vertex)
        for i in graph[next_vertex]:
            if i not in visited:
                to_visit.append(i)
    return visited

print(bfs('A'))