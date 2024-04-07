### 개념

* 특정 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구함
* 음의 간선이 없을 때만 정상적으로 동작함
* 동일한 형태의 작은 문제가 반복하여 나타나며, 부분 문제의 최적 결과가 전체 문제의 최적해를 낼 수 있으므로 [DP](DP.md) 를 활용한 알고리즘으로 볼 수 있음
* 방문하지 않은 노드 중, 비용이 적은 노드를 선택하여 
* 선형 탐색 방법과 우선순위 큐(Heap, Priority Queue)를 이용한 두 가지 방식으로 구현
* 모든 지점에서 다른 모든 지점까지의 최단 경로는 [Floyd-Warshall](Floyd-Warshall.md) 을 참고


---
### 구현 Linear Approach

* 시간복잡도 (N 은 정점의 개수) $$O(N^2)$$
* 정점의 개수는 많고, 간선의 개수는 적을 경우 시간이 오래걸릴 수 있음
* 구현 순서
	1. 출발 노드 설정
	2. 최단 거리 테이블 초기화
	3. 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드 선택
	4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여, 최단 거리 테이블 갱신
	5. 3 ~ 4 반복
	
```Python
def dijkstra(start_node, num_nodes):

	shortest_distance = [float('inf') for _ in range(num_nodes + 1)]
	shortest_distance[start_node] = 0
	visited = [False for _ in range(num_nodes + 1)]

	for _ in range(num_nodes):
		# 방문하지 않은 노드 중 최단거리 노드 선택
		min_distance = float('inf')
		min_node = 0
		for next_node in range(1, NUM_V + 1):
			if not visited[next_node] and shortest_distance[next_node] < min_distance:
				
				min_distance = shortest_distance[next_node]
				min_node = next_node

		# 해당 노드 방문 처리
		visited[min_node] = True

		# 해당 노드와 인접한 노드 갱신
		for adj_node, weight in adj_list[min_node]:
			if shortest_distance[adj_node] > shortest_distance[min_node] + weight:
				shortest_distance[adj_node] = shortest_distance[min_node] + weight

	return shortest_distance

```


---
### 구현 Priority Queue

* 시간 복잡도 $$O(NlogN)$$
* Heap 을 시용하여 PriorityQueue 구현
* 구현 순서는 선형 탐색과 동일하나, 선형탐색에서 최단 거리가 가장 짧은 노드를 선택하는 과정을 PriorityQueue 로 대체

```Python
import heapq

def dijkstra(start_node, num_nodes):

	shortest_distance = [float('inf') for _ in range(num_nodes + 1)]
	shortest_distance[start_node] = 0
	pq = [(0, start_node)]

	while pq:
		# 최단거리 노드 선택
		min_distance, min_node = heapq.heappop(pq)
		
		# 방문한 노드라면 스킵
		if min_distance > shortest_distance[min_node]:
			continue

		# 처음 방문하는 노드라면, 인접한 노드의 거리를 갱신
		else:
			for adj_node, weight in adj_list[min_node]:
				if shortest_distance[adj_node] > shortest_distance[min_node] + weight:
					shortest_distance[adj_node] = shortest_distance[min_node] + weight
					heapq.heappush(pq, (shortest_distance[min_node] + weight, adj_node))

	return shortest_distance
```


---
### 유형

1. Reverse Dijkstra
	* 다익스트라 정의는 특정 노드에서 → 나머지 노드까지의 최단 경로를 구하는 것
	* Reverse 는 모든 노드에서 → 특정 노드까지의 최단 경로를 구하는 것
		* 인접 리스트를 Reverse 로 생성하고(from, to 를 바꿈), '특정 노드' 를 출발점으로 다익스트라를 1회만 실행해도 나머지 노드까지의 최단경로를 알 수 있음
	* [BOJ파티](https://www.acmicpc.net/problem/1238)
	* [블로그 참조](https://chb2005.tistory.com/128)
2. 1차원 ~ 3차원 행렬
	1. 1차원  : Node 1 → N 으로 이동의 최단거리
	2. 2차원 : N X M 행렬 상에서 (1, 1) → (N, M) 으로 이동의 최단거리
	3. 3차원 : 실제 3차원 행렬 상에서 이동 혹은 방향성을 고려한 응용 문제 ([로봇](https://www.acmicpc.net/problem/1726))


---
### ⚠️ 주의

1. Queue 를 이용한 선형탐색 구현
	* 최단거리 노드에 대해 shortest_distance 가 업데이트될 때 마다, Queue 에 집어넣었음
	* 이 경우, 특정 노드가 여러번 큐에 추가될 수 있으므로 알고리즘 효율 저하
	* 또한 다익스트라 알고리즘은 최단 거리를 가진 노드를 우선적으로 방문해야 되는데, 단순 Queue 는 우선순위를 충족하기 어려움


---
### 참고


---
### 정리중