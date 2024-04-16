NUMBERS, MAX_DEPTH = map(int, input().strip().split(' '))
visited = []

def recursive(cur_depth, visited):
    if cur_depth == MAX_DEPTH:
        print(*visited, sep=" ")
    
    for i in range(1, NUMBERS + 1):
        if i not in visited:
            visited.append(i)
            recursive(cur_depth + 1, visited[::])
            visited.pop()

for i in range(1, NUMBERS + 1):
    visited.append(i)
    recursive(1, visited[::])
    visited.pop()
