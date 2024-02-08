########################################

graph = {
    1:[2,3],
    2:[4,5],
    3:[6,7],
    4:[8,9],
    5:[],
    6:[10],
    7:[11,12],
    8:[],
    9:[],
    10:[],
    11:[],
    12:[]
}
visited = []
to_visit = []

# # DFS - 1. list & stack
# to_visit.append(1)
# while to_visit:
#     vertex = to_visit.pop()
#     if vertex in visited:
#         continue
#     visited.append(vertex)
#     to_visit.extend(graph[vertex][::-1])

# print(visited)

# DFS - 2. deque
from collections import deque
visited = []
deque_to_visit = deque()

def dfs_deque(vertex):
    deque_to_visit.append(vertex)
    
    while deque_to_visit:
        vertex = deque_to_visit.pop()
        if vertex in visited:
            continue
        visited.append(vertex)
        deque_to_visit.extend(graph[vertex][::-1])

dfs_deque(1)
print(visited)


# DFS - 3. recursive
def dfs_recursive(vertex, visited = []):
    visited.append(vertex)
    for i in graph[vertex]:
        if i not in visited:
            dfs_recursive(i, visited)
    return visited

dfs_recursive(1)

# print(visited)