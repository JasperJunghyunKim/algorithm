### 개념

* 특정 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구함
* 음의 간선이 없을 때만 정상적으로 동작함
* 동일한 형태의 작은 문제가 반복하여 나타나며, 부분 문제의 최적 결과가 전체 문제의 최적해를 낼 수 있으므로 [[DP]] 를 활용한 알고리즘으로 볼 수 있음
* 방문하지 않은 노드 중, 비용이 적은 노드를 선택하여 
* 선형 탐색 방법과 우선순위 큐(Heap, Priority Queue)를 이용한 두 가지 방식으로 구현
* 모든 지점에서 다른 모든 지점까지의 최단 경로는 [[FloydWarshall]] 을 참고

### 구현_LinearApproach

* 시간복잡도 O(N^2)
	* 이때 N(Node) 은 정점의 수
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

### 구현_PriorityQueue

* 시간 복잡도 O(N log_N)
* Heap 을 시용하여 PriorityQueue 구현
* 구현 순서는 선형 탐색과 동일하나, 선형탐색에서 최단 거리가 가장 짧은 노드를 선택하는 과정을 PriorityQueue 로 대체

### 유형

### ⚠️ 주의
* 최단경로
* 

### 참고

### 정리중