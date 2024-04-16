### 개념

**MST(Minimum Spanning Tree)**
* Spanning Tree 란, 가중치가 부여된 무방향 그래프에서 <u>모든 정점을 포함하며 사이클이 없는 부분 그래프(Tree)</u> 를 의미
* 이러한 Spanning Tree 중에서 가중치의 합이 최소인 트리를 MST 라 함
* 따라서 N Vertex 의 MST 는, 반드시 N-1 Edge 를 가짐

**Kruskal**
* MST 를 구하는 대표적인 알고리즘
* 구현 순서
	1. Edge 를 가중치 기준으로 오름차순 정렬
	2. 가중치가 낮은 Edge 부터 선택하여, 사이클을 형성하지 않는 Edge 만 추가
		* 이때 사이클 형성 여부는 [Union Find](./Union%20Find) 알고리즘을 사용
	3. 이 과정을 Edge 의 수가 N - 1 (즉, Vertex 수가 N) 이 될 때까지 반복
* 알고리즘 활용
	* 통신 네트워크, 전력 그리드 등 인프라를 계획하는 문제에 사용됨
* [블로그 참고](https://chanhuiseok.github.io/posts/algo-33/)


### ⚠️ 주의 ⚠️


----
### 구현

```python
edge_list.sort(key = x : x(x[0])) # (weight, v_from, v_to)
num_edges_selected = 0

for w, v_from, v_to:
	if num_edges_selected = NUM_EDGES:
		break

	is_cycle = union(v_from, v_to) # return boolean
	if not is_cycle:
		num_edges_selected += 1
```

### 유형

1. [SWEA 1251 하나로](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15StKqAQkCFAYD)

### 참고

### 정리중