### 개념

* Depth First Search
* [그래프](wip%20Graph.md) 의 모든 노드를 체계적으로 탐색하는 알고리즘 중 하나로, 시작 정점으로부터 깊이를 우선적으로 탐색하며 가능한 멀리 있는 정점을 먼저 방문하고, 더 이상 방문할 정점이 없을 때 이전 분기점으로 돌아가 다른 경로를 탐색하는 방식
* 이를 위해 스택(Stack) 또는 재귀 호출을 사용
  **재귀 사용 권장**
*  모든 노드에 접근하기 때문에 [완전탐색](wip%20ExhaustiveSearch.md) 의 한 종류로 볼 수도 있으나, 구체적으로, BFS 는 효율적인 방법으로 문제를 해결하기 위해 사용됨
* DFS 는 모든 노드를 탐색하지만, 탐색 과정에서 Pruning(가지치기)를 적용하면 [wip BackTracking](wip%20BackTracking.md) 알고리즘으로 범위를 확장시킬 수 있음


---
### 구현_Stack

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
### 구현_Recursive (권장)

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
2. 


---
### ⚠️ 주의

1. [BOJ 1260](https://www.acmicpc.net/problem/1260)를 Stack 으로만 바꿔서 BFS 처럼 풀면, 문제 상 순회 순서 오류가 있음
2. 개인적으로 Recursive 방식을 권장


---
### 참고

### 정리중