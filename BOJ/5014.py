from collections import deque

heigth, start, end, up, down = map(int, input().strip().split(' '))

visited = [-1] * (heigth +  1)
to_visit = deque()
to_visit.append((start, 0))
visited[start] = 0

while to_visit:
    cur_floor, cur_cnt = to_visit.popleft()
    for next_floor in [cur_floor + up, cur_floor - down]:
        if 1 <= next_floor <= heigth:
            # if visited[next_floor] == -1 or visited[next_floor] > cur_cnt + 1:
            if visited[next_floor] == -1:
                to_visit.append((next_floor, cur_cnt + 1))
                visited[next_floor] = cur_cnt + 1
        else:
            continue

if visited[end] == -1:
    print('use the stairs')
else:
    print(visited[end])