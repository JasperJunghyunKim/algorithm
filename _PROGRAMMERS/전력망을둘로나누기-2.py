from collections import deque
is_connected = None
min_gap = float('inf')

def update_min_gap(n):
    global min_gap
    visited = [False for _ in range(n + 1)]
    groups = []
    for tower in range(1, n + 1):
        if not visited[tower]:
            visited[tower] = True
            to_visit = deque([tower])
            num_towers_in_group = 1
            while to_visit:
                cur_tower = to_visit.popleft()
                for next_tower in range(1, n + 1):
                    if is_connected[cur_tower][next_tower] and not visited[next_tower]:
                        visited[next_tower] = True
                        to_visit.append(next_tower)
                        num_towers_in_group += 1

            groups.append(num_towers_in_group)
    min_gap = abs(groups[0] - groups[1]) if abs(groups[0] - groups[1]) < min_gap else min_gap

def solution(n, wires):
    global is_connected
    is_connected = [[False] * (n + 1) for _ in range(n + 1)]
    for wire in wires:
        is_connected[wire[0]][wire[1]] = True
        is_connected[wire[1]][wire[0]] = True

    for wire in wires:
        is_connected[wire[0]][wire[1]] = False
        is_connected[wire[1]][wire[0]] = False
        update_min_gap(n)
        is_connected[wire[0]][wire[1]] = True
        is_connected[wire[1]][wire[0]] = True

    return min_gap

# n = 7
# wires = [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]
# print(solution(n, wires))