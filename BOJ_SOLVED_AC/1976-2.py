import sys
from collections import deque
sys_input = sys.stdin.readline

NUM_CITY = int(sys_input().strip())
NUM_BOUNDS = int(sys_input().strip())
graph = []
for _ in range(NUM_CITY):
    graph.append(list(map(int, sys_input().strip().split())))

route = list(map(lambda x: x-1, map(int, sys_input().strip().split())))

to_visit = deque([route[0]])
visited = [route[0]]
while to_visit:
    cur_city = to_visit.popleft()
    for next_city, is_connected in enumerate(graph[cur_city]):
        if is_connected and next_city not in visited:
                to_visit.append(next_city)
                visited.append(next_city)

for bound in route:
    if bound not in visited:
        print("NO")
        break
else:
    print("YES")