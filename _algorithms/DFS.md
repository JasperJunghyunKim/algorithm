### 개념

* Depth First Search
* [그래프](Graph.md) 의 모든 노드를 체계적으로 탐색하는 알고리즘 중 하나로, 시작 정점으로부터 깊이를 우선적으로 탐색하며 가능한 멀리 있는 정점을 먼저 방문하고, 더 이상 방문할 정점이 없을 때 이전 분기점으로 돌아가 다른 경로를 탐색하는 방식
* 이를 위해 스택(Stack) 또는 재귀 호출을 사용 → **재귀 사용 권장**
* (특정 조건을 만족할 때 까지) 모든 노드에 접근하기 때문에 [완전탐색](Exhaustive%20Search.md) 의 한 종류로 볼 수도 있음
* DFS 는 모든 노드를 탐색하지만, 탐색 과정에서 Pruning(가지치기)를 적용하면 [BackTracking](BackTracking.md) 알고리즘으로 범위를 확장시킬 수 있음


### ⚠️ 주의

1. 코드 직관성, 순서 보장을 위해선 재귀적으로 구현하는 것이 편리
	* [BOJ 1260](https://www.acmicpc.net/problem/1260)에서 Stack 으로 구현해볼 것 → 순서 보장하기 어려움
2. 단, 재귀적으로 구현하기 위해선 stack overflow 를 조심해야 함
	* 특히 Python 은 기본 recursion limit 이 1000 으로 매우 작기 때문에, recursion error 가 발생하기 쉬움
	* `sys.setrecursionlimit(N)`
3. 최단 경로를 찾는 문제는 [BFS](BFS.md) 또는 [Dijkstra](Dijkstra.md) 를 사용할 것
	* DFS 는 깊이 있는 경로를 따라가는 중에, 최단 경로보다 훨씬 더 길거나 비효율적인 경로를 여러번 탐색하게 될 수 있음(반면 BFS 는 최단경로를 찾는 순간 Queue를 종료)
	* DFS 는 최초로 목적지 노드에 도달했을 때, 해당 깊이가 반드시 최단거리임을 보장하지 않음 → 모든 노드를 방문하고 비교했을 때만 해당 노드가 최단 거리임을 알 수 있으므로 비효율적임


---
### 구현 Stack

```Python
dfs_visited = [START_V]
dfs_to_visit = [START_V]
while dfs_to_visit:
	cur_v = dfs_to_visit.pop() # stack
	for next_v in range(1, NUM_V + 1):
		if graph[cur_v][next_v] == True and next_v not in dfs_visited:
			dfs_visited.append(next_v)
			dfs_to_visit.append(next_v)

print(*dfs_visited)
```


---
### 구현 Recursive (권장)

* 개인적으로 DFS 는 재귀적으로 구현하는 것이 더 직관적임
* 또한 방문 순서의 보장이 필요한 경우 재귀함수가 더 간결함

```Python
dfs_visited = [START_V]

def dfs(cur_v):
	for next_v in range(1, NUM_V + 1):
		if graph[cur_v][next_v] == True and next_v not in dfs_visited:
			dfs_visited.append(next_v)
			dfs(next_v)
			
dfs(START_V)
print(*dfs_visited)
```


---
### 유형

1. [BOJ 1260](https://www.acmicpc.net/problem/1260)
2. 그래프 사이클 찾는 문제 (탐색 도중 백엣지가 존재하면 사이클이 존재하는 것)


---
### 참고

### 정리중