### Disjoint Set (분리 집합 ) 개념

* 여러 개의 원소가 주어졌을 때, 이들을 서로 겹치지 않는 부분 집합들로 나누고, 각 집합의 정보를 관리하는 자료구조
* 이 자료구조는 각 집합을 대표하는 '대표 원소(representative)' 또는 '루트(root)'를 사용해 각 집합을 구별함


---
### Union Find 개념

- 두 개의 원소가 같은 집합에 속하는지 빠르게 판별하기 위해 사용되는 알고리즘
  주로 네트워크 연결, 최소 신장 트리, 그래프 사이클 검사 등과 같은 그래프 이론에서 활용됨
* Disjoint Set 을 구현하기 위한 알고리즘이며, 세 가지 주요 연산이 있음
	1. make_set
	2. union
	3. find
* 즉, 본 알고리즘은 원소 간의 관계(특히 서로소 관계)를 파악할 수 있게 해줌


---
### 구현_기본

1. **make_set** 
	* 각각의 N 개 원소에 대하여 대표(즉, root)가 되도록 하는 N 개의 집합을 생성
2. **find(x)** 
	* 원소 x 의 root 를 찾음
	* 즉, 원소 x 가 어떤 집합에 포함 되었는지 찾는 함수
1. **union(x, y)**
	* y 의 root 를 x 의 root 로 설정하여, 같은 집합이 되도록 하는 함수
	* root 에 대한 연산
``` Python 3
# make_set
for i in range(1, n + 1):
	root[i] = i

# find
def find(x):
	if root[x] == x:
		return x
	return find(root[x])

# union
def union(x, y):
	root_x = find(x)
	root_y = find(y)
	root[root_y] = root_x
```


---
### 구현_최적화(Path Compression, Union By Rank)

1. **경로 압축(Path Compression)**
   Find 연산을 실행하면서 만나는 모든 노드가 직접 루트를 가리키도록 함으로써 Find 연산의 속도를 개선
2. **Union By Rank**
   두 트리를 합칠 때 높이(랭크)가 더 낮은 트리를 높이가 더 높은 트리 아래에 붙이는 방식으로, 트리의 높이 증가를 최소화
```python
# find - path compression
def find(n):
	if root[n] == n:
		return n
	root[n] = find(root[n])
	return root[n]

# union - union by rank
# append shorter subtree to another one
def union(a, b)
	root_a = find(a)
	root_b = find(b)
	if root_a == root_b:
		return
	if depth[root_a] > depth[root_b]:
		root[root_b] = root_a
	elif depth[root_a] < depth[root_b]:
		root[root_a] = root_b
	else:
		root[root_b] = root_a
		depth[root_a] += 1
```


---
### 유형
1. 두 집합이 합쳐지면서 capacity 가 늘어나고, 해당 집합에 포함되는 대상의 개수(size)가 capacity 를 초과하지 않는지를 확인하는 문제
	- [방청소](https://www.acmicpc.net/problem/9938)
2. [Kruskal (MST)](Kruskal%20(MST).md) MST 알고리즘


---
### ⚠️ 주의

### 참고

### 정리중
