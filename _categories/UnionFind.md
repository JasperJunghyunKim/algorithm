##### A. 원리
##### B. 접근, 구현 방법
* 기본 구현 방법
* path compression, subtree depth comparison
* [방청소](https://www.acmicpc.net/problem/9938) 문제와 같이, 경우에 따라 capacity 와 size 를 저장해주는 경우도 있음 
``` Python
# find - 기본
def find(n):
	if root[n] == n:
		return n
	return find(root[n])

# union - 기본
def union(a, b):
	root_a = find(a)
	root_b = find(b)
	root[root_b] = root_a
```

```python
# find - path compression
def find(n):
	if root[n] == n:
		return n
	root[n] = find(root[n])
	return root[n]

# union - subtree's depth comparison
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

##### C. 유형
* [방청소](https://www.acmicpc.net/problem/9938)
##### D. 정리중
Disjoint Set과 Union Find 알고리즘은 서로 밀접하게 연관된 개념입니다. 이들은 집합을 효율적으로 관리하고, 두 원소가 같은 집합에 속하는지 빠르게 판별하기 위해 사용됩니다. 이 개념들은 주로 네트워크 연결, 최소 신장 트리, 그래프의 사이클 검사 등과 같은 그래프 이론에서 활용됩니다.

### Disjoint Set (분리 집합)

Disjoint Set은 여러 개의 원소가 주어졌을 때, 이들을 서로 겹치지 않는 부분 집합들로 나누고, 각 집합의 정보를 관리하는 자료구조입니다. 이 자료구조는 각 집합을 대표하는 '대표 원소(representative)' 또는 '루트(root)'를 사용해 각 집합을 구별합니다.

### Union Find 알고리즘

Union Find 알고리즘은 Disjoint Set을 구현하는 알고리즘으로, 주로 두 가지 주요 연산을 제공합니다:

1. **Union**: 두 원소가 속한 집합을 합치는 연산입니다. 두 원소가 이미 같은 집합에 속해 있으면 아무 것도 하지 않고, 그렇지 않은 경우 두 집합을 하나로 합칩니다.

2. **Find**: 주어진 원소가 속한 집합의 대표 원소(루트)를 찾는 연산입니다. 이 연산은 주어진 두 원소가 같은 집합에 속해 있는지 여부를 판별하는 데에도 사용됩니다.

### 관계

- **Disjoint Set은 개념**입니다. 여러 원소가 겹치지 않는 부분 집합으로 구분되어 있을 때, 각 집합의 정보를 효율적으로 관리하는 자료구조의 개념을 의미합니다.

- **Union Find는 Disjoint Set을 구현하는 알고리즘**입니다. Union과 Find 연산을 통해 Disjoint Set의 각 집합을 관리하고, 원소 간의 관계를 효율적으로 파악할 수 있게 해 줍니다.

Union Find 알고리즘의 효율성을 높이기 위해 사용되는 기법으로는 **경로 압축(Path Compression)**과 **랭크(Rank) 기반의 합치기(Union by Rank)**가 있습니다. 경로 압축은 Find 연산을 실행하면서 만나는 모든 노드가 직접 루트를 가리키도록 함으로써 Find 연산의 속도를 개선합니다. 랭크 기반 합치기는 두 트리를 합칠 때 높이(랭크)가 더 낮은 트리를 높이가 더 높은 트리 아래에 붙이는 방식으로, 트리의 높이 증가를 최소화합니다. 이러한 최적화 기법들은 Union Find 알고리즘의 성능을 크게 향상시킵니다.

