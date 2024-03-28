


https://www.notion.so/59163bcc496c47b790773e312409f364?pvs=4


[알고리즘 공부 순서 VELOG](https://velog.io/@cxxerry/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B3%B5%EB%B6%80-%EC%88%9C%EC%84%9C)
[알고리즘 공부 순서 - 문제 정리](https://patiencelee.tistory.com/1072)
[한 장으로 보는 알고리즘 공부 순서](https://velog.io/@ngngs/%ED%95%9C-%EC%9E%A5%EC%9C%BC%EB%A1%9C-%EB%B3%B4%EB%8A%94-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98)


# 복잡도 계산
* [코드의 시간 복잡도 계산하기 MEDIUM](https://medium.com/humanscape-tech/%EC%BD%94%EB%93%9C%EC%9D%98-%EC%8B%9C%EA%B0%84-%EB%B3%B5%EC%9E%A1%EB%8F%84-%EA%B3%84%EC%82%B0%ED%95%98%EA%B8%B0-b67dd8625966)
* [빅오 표기법을 설명하다 - 시간과 공간의 복잡도](https://www.freecodecamp.org/korean/news/big-o-notation-why-it-matters-and-why-it-doesnt-1674cfa8a23c/)
* [Complexity Cheat Sheet](https://www.bigocheatsheet.com/)
* [Practice Questions](https://www.geeksforgeeks.org/practice-questions-time-complexity-analysis/)

1. 시간복잡도
2. 공강복잡도
	- 메모리 사용량 계산

# Python 자료 구조
1. List
2. Set
3. 해시테이블 Dict
4. Queue, Stack
5. Heap
6. Tree
7. 

# 유형
1. DP
2. 그래프 이론
	- 인접
1. BFS, DFS
2. 백트래킹
3.  완전탐색 (Exhaustive Search)
	* Brute Force
	* 비트마스크
	* 재귀함수를 이용한 백트래킹
	* 순열을 이용해서 모든 경우를 중복 없이 다 해보는 방법
	* BFS / DFS
	* Meet In the Middle (BOJ 1208, 7453, 1450)
4. 그래프 이론
	- 인접 행렬, 인접 리스트, 간선 리스트
5. 그래프 이론 2
	- 다익스트라, 플로이드워셜, 벨만포드
	- 최소 신장 스패닝 트리(MST), 크루스칼
	- 이분그래프(Bipartite Graph)
		- BFS
		- 이분그래프 찾는 방법
		- 연결 그래프인지, 비연결 그래프인지 구분
	- [순환 그래프](https://jackpot53.tistory.com/92)
	- 
1. 그리디 알고리즘
2. 순열, 조합, 중복순열, 중복조합
3. 문자열
4. 분할정복
	- 이분탐색, 머지 소트, 퀵 소트
5. 이분탐색
6. Union Find, Disjoint Set
7. Flood Fill
8. 정렬
9. 트리
	- 순회 종류 : Pre, In, Post)
	- 트리 지름 계산
10. 진법변환
11. Heap, Priority Queue
12. 문자열 알고리즘
	- KMP
13. 수학
	- 소수, 최소공배수, 최대공약수, 소인수분해, 팩토리얼
14. 구간 최소값
	- 슬라이딩 윈도우 알고리즘, 세그먼트 트리, DP, 루트 N 으로 나누기, 2차원 배열에 저장하는 방법, 다 해보는 방법


-----------
# BFS, DF
# Back Tracking
###### 원리
* 재귀함수를 이용한 DFS
###### 구현 방법
###### 유형
- N 과 M 순열
- N Queen
- 

-----

# DP
##### A. 원리
- 문제를 나누고, 그 문제의 결과 값을 재활용하여 전체 답을 구함
- 동일한 작은 문제들이 반복하여 나타나는 경우에 사용 가능
- 부분 문제의 최적 결과값이 전체 문제의 최적 결과를 낼 수 있는 경우 사용 가능
##### B. 접근, 구현 방법
1. 점화식 만들기
	* 점화식(일반적으로 DP 배열)의 의미부터 정리
	* 예) i 번째까지 실행했을 때의 최적해
2. Bottom Up (Tabulation)
	- 직관적으로 접근 가능 (선형적으로 해결하므로)
	- 반복적으로 부분 문제를 해결하고, 결과를 배열 등에 저장
3. Top Down (Recursive) + Memoization
4. Memoization
##### C. 유형
- 피보나치 수
- 0-1 Knapsack Problem
- 최장증가부분수열
- N x M 배열 간 영향을 주는 점화식
##### D. 정리필요
- 구현 방법 Bottom Up, Top Down 비교
	- 둘 다 점화식은 동일
	- 구현 방법에 있어선 Bottom Up 방식이 비교적 직관적으로 접근 가능 -> Linear 하게 해결하므로
	- 그러나 Top Down 은 재귀 함수를 사용하므로 Recursive Error 가 발생할 수 있음
	- 메모리 접근
	- ... 반면 Top Down 는 필요한 부분만 해결하므로 성능적으로 우수할 수 도 있음
	- ...
	- ...
	- 동적 프로그래밍(Dynamic Programming, DP) 문제를 풀 때 Top-down(메모이제이션) 방식과 Bottom-up(타뷸레이션) 방식을 선택할 수 있으며, 두 방식은 각각 재귀 함수와 반복문을 기반으로 합니다. 이론적으로, 두 방식이 해결하는 서브 문제의 수와 연산의 양이 같다면, 시간 복잡도는 동일합니다. 그러나 실제로는 몇 가지 이유로 인해 성능 차이가 발생할 수 있습니다:
	
	1. **함수 호출 오버헤드**: Top-down 방식은 재귀 함수 호출을 사용하기 때문에, 함수 호출 스택과 관련된 오버헤드가 발생합니다. 반면, Bottom-up 방식은 반복문을 사용하므로 이러한 오버헤드가 없습니다. 따라서, 같은 문제를 해결할 때 Bottom-up 방식이 좀 더 효율적일 수 있습니다.
	
	2. **메모리 접근 패턴**: Bottom-up 방식은 일반적으로 메모리에 순차적으로 접근합니다. 이는 CPU 캐시 활용성을 높여 성능을 향상시킬 수 있습니다. Top-down 방식에서는 재귀의 깊이와 순서에 따라 메모리 접근 패턴이 불규칙할 수 있어, 상대적으로 캐시 효율이 떨어질 수 있습니다.
	
	3. **스택 오버플로**: 깊은 재귀를 사용하는 Top-down 방식은 스택 오버플로를 일으킬 위험이 있습니다. 특히, 문제의 크기가 매우 클 경우 이러한 위험이 커집니다. Bottom-up 방식은 이러한 제한이 없습니다.
	
	4. **서브 문제의 재사용**: Top-down 방식은 필요한 서브 문제만을 정확히 해결하여 메모이제이션합니다. 반면, Bottom-up 방식은 모든 서브 문제를 처음부터 차례대로 해결합니다. 따라서, 특정 조건에서는 Top-down 방식이 더 적은 수의 서브 문제를 해결함으로써 성능 이점을 가질 수 있습니다.
	
	결론적으로, Top-down과 Bottom-up 방식 모두 동일한 문제를 해결하기 위해 동일한 수의 서브 문제를 해결하지만, 함수 호출 오버헤드, 메모리 접근 패턴, 스택 오버플로의 위험 등의 차이로 인해 실제 실행 시간에서 차이가 발생할 수 있습니다. 일반적으로 Bottom-up 방식이 더 효율적이라고 평가되는 경우가 많으나, 실제 성능은 문제의 성격, 구현 방법, 사용 환경에 따라 달라질 수 있습니다. 따라서, 어떤 방식이 더 나은지를 판단하기 위해서는 직접 구현해보고 성능을 비교하는 것이 좋습니다.






---


---
# 그래프 이론 1
##### A. 원리
##### B. 접근, 구현 방법
* [그래프 저장 방법](https://velog.io/@eunchae2000/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EA%B7%B8%EB%9E%98%ED%94%84%EB%A5%BC-%EC%A0%80%EC%9E%A5%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95-3%EA%B0%80%EC%A7%80-%EC%9D%B8%EC%A0%91-%ED%96%89%EB%A0%AC-%EC%9D%B8%EC%A0%91-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EA%B0%84%EC%84%A0-%EB%A6%AC%EC%8A%A4%ED%8A%B8-with-Python)
* 인접 행렬
* 인접 리스트
* 간선 리스트
* 가중치 유무
* 방향성 유무
##### C. 비교
##### D. 유형
- BFS
- DFS
- 다익스트라(Dijkstra)
- 크루스칼(Kruskal)
- 플로이드 워셜
- 벨만 포드
- 위상정렬


---
# 그리디 알고리즘
* 그리디 적용 가능성 확인
	1. 분할 가능
	2. 지역 최적해가 전역 최적해를 보장




---
# Union Find
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



# Divide Conquer
###### 원리
* 
###### 접근 방법 / 구현 방법
1. Divide
	- 하위 문제로 분할 가능할 때까지 나눔
2. Conquer
	- 하위 문제를 재귀적으로 해결
	- 나눌 수 없는 단위가 되면, 탈출 조건을 설정하고 문제를 해결
3. Combine

###### 구현 비교

###### 유형

###### 정리중

1. 구현 비교
2. 유형
	* Quick Sort, Merge Sort, Binary Search
3. 정리중



# 조합, 순열, 중복 순열, 중복 조합



##### 24-03-19
- DFS 와 백트래킹
	- 여행경로
	- N Queen
	- N 과 M

* combination, permutation


- 전역 참조가 불가하면 list[0] 인덱스를 사용하는 방법
- 최단거리는 BFS / 다익스트라 사용
	DFS(깊이 우선 탐색)를 사용하여 최단 거리 문제를 해결할 때 성능이 좋지 않은 주된 이유는, DFS가 모든 가능한 경로를 탐색하기 때문에 비효율적으로 많은 시간을 소모할 수 있기 때문입니다. 특히, 최단 거리를 찾는 문제의 경우에는 더욱 그렇습니다. 다음은 DFS 사용 시 성능이 좋지 않은 구체적인 이유들입니다:

1. **비효율적인 경로 탐색**: DFS는 한 방향으로 가능한 깊숙이 탐색을 진행한 후에야 다른 방향을 탐색합니다. 이 과정에서 최단 경로와는 크게 벗어난 긴 경로를 먼저 탐색할 수 있으며, 최단 경로가 아닌 많은 경로들을 불필요하게 탐색하게 됩니다.

2. **중복 탐색**: 특정 노드를 방문했을 때, 이 노드를 통해 도달할 수 있는 다른 노드들에 대한 탐색을 반복적으로 수행할 수 있습니다. 특히, 사이클이 있는 그래프에서는 무한 반복의 위험이 있습니다. 최단 거리 문제에서는 방문했던 노드를 또 다시 방문하는 것이 대부분 불필요하므로, 이러한 중복 탐색은 많은 시간 낭비를 야기합니다.

3. **최단 거리 보장 불가**: DFS는 모든 경로를 탐색하긴 하지만, 최초로 목적지에 도달했을 때의 경로가 반드시 최단 거리임을 보장하지 않습니다. 따라서, 모든 가능한 경로를 탐색한 후에야 최단 거리를 판별할 수 있으며, 이는 매우 비효율적입니다.

4. **자원 소모**: DFS는 재귀 호출을 많이 사용하게 되는데, 이는 호출 스택의 크기를 증가시키고, 결국 스택 오버플로를 일으킬 위험을 증가시킵니다. 또한, 많은 메모리를 소모할 수 있습니다.

	최단 거리 문제에서는 보통 BFS나 다익스트라 알고리즘 같은 다른 알고리즘이 훨씬 더 효율적입니다. BFS는 레벨 별로 탐색을 진행하기 때문에, 최초로 목적지에 도달했을 때의 경로가 최단 거리임을 보장합니다. 다익스트라 알고리즘은 가중치가 있는 그래프에서 최단 거리를 찾는데 사용됩니다.
* 


###### 23-03-18
* 

###### 문제
- [BOJ 14500](https://www.acmicpc.net/problem/14500)
	- DFS 재귀 전후 visited check 조건


###### 23-03-16
* 참조형 vs (?) / 그리고 전역 범위

* max(2D graph)





# Python 구현
1. 배열 Deep Copy, slicing
``` Python
a = [1,2,3]
b = a[::]
```
2. list append 시 메모리 재할당 발생
		https://atelier-house.tistory.com/3
1. sys.stdin.readline / input 차이
2. sys.stdout.write / print 차이
3. tuple 로 구성된 list 정렬
	- 정렬 기준 : tuple 의 두 번째 원소 → 첫 번째 원소 순서
``` python
list().sort(key = lambda x : (x[1], x[0]))
```
6. dict keys, dict values, dict items
7. swap
``` python
a = 10, b = 20
a, b = b, a
print(a, b) # 20, 10
```
8. sort vs sorted
9. itertools - combinations, permutations
10. visited 구현
	* x is in list() 대신, boolean list 로 구현
11. enumerate