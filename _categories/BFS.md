##### 개념
* 그래프, 트리 등의 자료구조의 대표적인 탐색 알고리즘
* 
##### 구현_Queue
```Python
bfs_visited = [START_V]
bfs_to_visit = deque([START_V])

while bfs_to_visit:
	cur_v = bfs_to_visit.popleft()
	for next_v in range(1, NUM_V + 1):
		if adj_maxtrix[cur_v][next_v] == True and next_v not in bfs_visited:
			bfs_visited.append(next_v)
			bfs_to_visit.append(next_v)

print(*bfs_visited, sep=" ")
```
##### 유형
##### 정리중

