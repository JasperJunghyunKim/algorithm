### 개념

* 모든 지점에서 다른 모든 지점까지의 최다 경로를 구하는 알고리즘
* 2 차원 테이블에 최단 거리 정보를 저장 → 모든 지점 간 거리를 저장해야 되므로
* 노드 개수 N 번 만큼 반복하며 점화식에 맞게 2 차원 리스트를 갱신하므로, [DP](./DP.md) 알고리즘에 속함
	* 각 N 번째 노드에 대하여, N 번 노드를 거쳐가는 경우를 고려하여 테이블을 갱신
* 시간복잡도가 O(N^3) 이므로, 그래프의 크기가 작은 경우에 적합
* 특정 지점에서 다른 모든 지점까지의 최단 경로는 [Dijkstra](./Dijkstra.md) 를 참고

### 구현

* 기본 점화식 $$D_{ab} = min(D_{ab} ,  D_{ak} + D_{kb})$$
* 1 ~ N 을 순회하는 i 번째 노드에 대하여, 노드 a → b 의 경로와 a → i → b 를 비교
* 시간복잡도
	* 각 N 개의 노드마다, O(N^2) 연산을 하므로
		$$O(N^3)$$
```Python
graph = [[float('inf') for _ in range(NUM_V + 1)] for _ in range(NUM_V + 1)]

for i in range(NUM_V + 1):
	graph[i][i] = 0

for _ in range(NUM_E):
	v_from, v_to, weight = map(int, sys_input().split())
	graph[v_from][v_to] = weight

# Floyd-Warshall
for stopover in range(1, NUM_V + 1):
	for x in range(1, NUM_V + 1):
		for y in range(1, NUM_V + 1):
			graph[x][y] = min(graph[x][y], graph[x][stopover] + graph[stopover][y])
```

### 유형

1. ...

### ⚠️ 주의

1. ...
	
### 참고

* [블로그1](https://blog.naver.com/ndb796/221234427842)
* [블로그2](https://velog.io/@kimdukbae/%ED%94%8C%EB%A1%9C%EC%9D%B4%EB%93%9C-%EC%9B%8C%EC%85%9C-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Floyd-Warshall-Algorithm)

### 정리중