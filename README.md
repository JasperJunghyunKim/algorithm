
https://www.notion.so/59163bcc496c47b790773e312409f364?pvs=4


[알고리즘 공부 순서 VELOG](https://velog.io/@cxxerry/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B3%B5%EB%B6%80-%EC%88%9C%EC%84%9C)
[알고리즘 공부 순서 - 문제 정리](https://patiencelee.tistory.com/1072)
[한 장으로 보는 알고리즘 공부 순서](https://velog.io/@ngngs/%ED%95%9C-%EC%9E%A5%EC%9C%BC%EB%A1%9C-%EB%B3%B4%EB%8A%94-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98)


### 복잡도 계산
[코드의 시간 복잡도 계산하기 MEDIUM](https://medium.com/humanscape-tech/%EC%BD%94%EB%93%9C%EC%9D%98-%EC%8B%9C%EA%B0%84-%EB%B3%B5%EC%9E%A1%EB%8F%84-%EA%B3%84%EC%82%B0%ED%95%98%EA%B8%B0-b67dd8625966)
[빅오 표기법을 설명하다 - 시간과 공간의 복잡도](https://www.freecodecamp.org/korean/news/big-o-notation-why-it-matters-and-why-it-doesnt-1674cfa8a23c/)
[Complexity Cheat Sheet](https://www.bigocheatsheet.com/)
[Practice Questions](https://www.geeksforgeeks.org/practice-questions-time-complexity-analysis/)

1. 시간복잡도
2. 공강복잡도
	- 메모리 사용량 계산

### Python 자료 구조
1. List
2. Set
3. 해시테이블 Dict
4. Queue, Stack
5. Heap
6. Tree
7. 

### 유형
1. DP
2. BFS, DFS
3. 백트래킹
4.  완전탐색 (Exhaustive Search)
	* Brute Force
	* 비트마스크
	* 재귀함수를 이용한 백트래킹
	* 순열을 이용해서 모든 경우를 중복 없이 다 해보는 방법
	* BFS / DFS
	* Meet In the Middle (BOJ 1208, 7453, 1450)
5. 그래프 이론
	- 인접 행렬, 인접 리스트, 간선 리스트
6. 그래프 이론 2
	- 다익스트라, 플로이드워셜, 벨만포드
	- 최소 신장 스패닝 트리(MST), 크루스칼
1. 그리디 알고리즘
3. 순열, 조합, 중복순열, 중복조합
4. 문자열
5. 분할정복
	- 이분탐색, 머지 소트, 퀵 소트
6. 이분탐색
7. Union Find
8. Flood Fill
9. 정렬
10. 트리
	- 순회 종류 : Pre, In, Post)
	- 트리 지름 계산
11. 진법변환
12. Disjoint Set
13. Heap, Priority Queue
14. 문자열 알고리즘
15. 수학
	- 소수, 최소공배수, 최대공약수, 소인수분해, 팩토리얼
16. 구간 최소값


# DP
- dp 점화식이 의미하는 정의를 먼저 정할 것
	- 예) dp\[i\] 는 
- 점화식은 2차원 행렬이 될 수도 있다 (여러 조건이 추가되면)
	- 예) 0-1 Knapsack 문제처럼
- 연산 최소값을 구하시오
- Knapsack Problem
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
* 


### 그리디 알고리즘
* 그리디 적용 가능성 확인
	1. 분할 가능
	2. 지역 최적해가 전역 최적해를 보장
1

백 트래킹

### 조합, 순열, 중복 순열, 중복 조합



##### 24-03-19
- DFS 와 백트래킹
	- 여행경로
	- N Queen
	- N 과 M
* dict keys
* dict items
* dict values>
* 집합 ... iter 종류 재확인
* https://medium.com/@chullino/if-name-main-%EC%9D%80-%EC%99%9C-%ED%95%84%EC%9A%94%ED%95%A0%EA%B9%8C-bc48cba7f720
* DP 시, bottom up, top down 적합 조건
* combination, permutation
* list.count


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
* N QUEEN - 
* 

###### 문제
- [BOJ 14500](https://www.acmicpc.net/problem/14500)
	- DFS 재귀 전후 visited check 조건
- [BOK]()
- 


###### 23-03-16
* 참조형 vs (?) / 그리고 전역 범위
* swap 한번에
* combination, perm
* max(2D graph)
* BFS, DFS 꼴 복습
* 'meetings.sort(key=lambda x: (x[1], x[0]))'
* 

###### 23-03-15
- BFS, DFS
- Divide Conquer
- 자료구조 불변

## 자료구조
- 스택
- 덱
- 


## DP
- 재귀 (top down)
- 메모이제이션 점화식 (bottom up)
- 

## 사용법
- 각 컬렉션 ... 등의 추가, 제거 방법


## 코드

```python

import sys
input = sys.stdin.readline

n = int(input())

```


### 익힐것
* 슬라이싱
* 키 밸류 같이 출력하는 거
* sys.stdin.readline / input 차이
* sys.stdout.write / print 차이
* strip
* append 시 메모리 재할당이 발생하므로 메모리를 효율적으로 사용하지 못함
* enumerate


## 참고사항
* visited 체크를 꼭 is in 으로 확인하지 말고, index + boolean 적용해서 시간 단축


```python

a = [1,2,3,4,5]
b = a
c = a[::]

print(id(a))
print(id(b))
print(id(c))

b.append(6)
print(b)
print(a)

  

c.append(7)
print(c)
print(a)

```


### 수학
* itertools - combinations, permutations