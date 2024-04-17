import sys
sys_input = sys.stdin.readline

NUM_EVENTS, NUM_REL = map(int, sys_input().strip().split())
graph = {i: [] for i in range(1, NUM_EVENTS + 1)}
for _ in range(NUM_REL):
    event_before, event_after = map(int, sys_input().strip().split())
    graph[event_before].append(event_after)

def dfs(cur_event):
    if visited[cur_event]:
        return
    visited[cur_event] = True
    for next_event in graph[cur_event]:
        if not visited[next_event]:
            dfs(next_event)
            events_after[cur_event] |= {next_event}
            events_after[cur_event] |= events_after[next_event]

events_after = [set() for _ in range(NUM_EVENTS + 1)]
visited = [False for _ in range(NUM_EVENTS + 1)]
for i in range(1, NUM_EVENTS + 1):
    dfs(i)

for _ in range(int(sys_input().strip())):
    event_a, event_b = map(int, sys_input().strip().split())
    if event_b in events_after[event_a]:
        print(-1)
    elif event_a in events_after[event_b]:
        print(1)
    else:
        print(0)