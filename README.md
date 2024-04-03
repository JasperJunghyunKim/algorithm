


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
	- 메모리 사용량 계산 https://zoosso.tistory.com/995


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






# 조합, 순열, 중복 순열, 중복 조합






- 전역 참조가 불가하면 list[0] 인덱스를 사용하는 방법
- 최단거리는 BFS / 다익스트라 사용
	DFS(깊이 우선 탐색)를 사용하여 최단 거리 문제를 해결할 때 성능이 좋지 않은 주된 이유는, DFS가 모든 가능한 경로를 탐색하기 때문에 비효율적으로 많은 시간을 소모할 수 있기 때문입니다. 특히, 최단 거리를 찾는 문제의 경우에는 더욱 그렇습니다. 다음은 DFS 사용 시 성능이 좋지 않은 구체적인 이유들입니다:

1. **비효율적인 경로 탐색**: DFS는 한 방향으로 가능한 깊숙이 탐색을 진행한 후에야 다른 방향을 탐색합니다. 이 과정에서 최단 경로와는 크게 벗어난 긴 경로를 먼저 탐색할 수 있으며, 최단 경로가 아닌 많은 경로들을 불필요하게 탐색하게 됩니다.

2. **중복 탐색**: 특정 노드를 방문했을 때, 이 노드를 통해 도달할 수 있는 다른 노드들에 대한 탐색을 반복적으로 수행할 수 있습니다. 특히, 사이클이 있는 그래프에서는 무한 반복의 위험이 있습니다. 최단 거리 문제에서는 방문했던 노드를 또 다시 방문하는 것이 대부분 불필요하므로, 이러한 중복 탐색은 많은 시간 낭비를 야기합니다.

3. **최단 거리 보장 불가**: DFS는 모든 경로를 탐색하긴 하지만, 최초로 목적지에 도달했을 때의 경로가 반드시 최단 거리임을 보장하지 않습니다. 따라서, 모든 가능한 경로를 탐색한 후에야 최단 거리를 판별할 수 있으며, 이는 매우 비효율적입니다.

4. **자원 소모**: DFS는 재귀 호출을 많이 사용하게 되는데, 이는 호출 스택의 크기를 증가시키고, 결국 스택 오버플로를 일으킬 위험을 증가시킵니다. 또한, 많은 메모리를 소모할 수 있습니다.

	최단 거리 문제에서는 보통 BFS나 다익스트라 알고리즘 같은 다른 알고리즘이 훨씬 더 효율적입니다. BFS는 레벨 별로 탐색을 진행하기 때문에, 최초로 목적지에 도달했을 때의 경로가 최단 거리임을 보장합니다. 다익스트라 알고리즘은 가중치가 있는 그래프에서 최단 거리를 찾는데 사용됩니다.






# Python 구현 팁

1. Deep Copy + Slicing
	
	``` Python
	a = [1,2,3]
	b = a[::]
	```


2. Visited Check 성능 비교
	
	* BFS, DFS, FloodFill, BackTracking 등에서 사용되는 Visited 사용 방법
	* 리스트, 딕셔너리를 활용한 특정 좌표의 visited 여부 체크 방법
	* 아래 두 코드는 모두 동일하게 특정 튜플 (1,2) 의 방문 여부룰 체크함
	* 그러나 딕셔너리는 내부적으로 #해시테이블 을 사용하므로, 키 존재 여부를 평균 O(1) 으로 확인 가능
	* 반면, 리스트는 각 원소를 처음부터 순차적으로 비교하므로, 최악의 경우 O(n) 소요
``` Python
	visited_a = [(1,2), (2,3), (3,4)] 
	print((1,2) in a)

	visited_b = {(1,2): True, (2,3): True, (3,4): True}
	print((1,2) in b)
```


3. 전역 변수 사용
	
	**기본 자료형 (Prinimtive Type)**
	- 기본 자료형은 전역적으로 사용할 수 없음
	- 따라서 특정 함수 내부에서 변수에 접근(조회, 수정)하기 위해선 해당 변수를 전역 #global 선언 하거나, 
	- \[Cheat\] 값 자체를 길이 1 인 리스트 (a = \[0\]) 로 선언하여 전역 처럼 접근하는 방법이 있음
	
	**참조형 자료형(Reference Type)**
	* deque, list, dict 등은 기본적으로 전역 변수로 선언된 인스턴스를 참조함
	* 따라서 함수 내부에서 사용할 때, #global 키워드 없이도 인스턴스에 접근이 가능함 (조회, 수정 가능)
	* \[중요\] 그러나 새로운 객체를 할당하는 것은 변수를 직접 수정하는 것과 같으므로, 이 경우엔 #global 키워드를 사용해 전역 변수로 명시해야 함
		``` Python
		my_list = [1, 2, 3] 
		def update_list(): 
			my_list.append(4) # 전역 변수의 내용을 변경 
		def replace_list(): 
			global my_list 
			my_list = [4, 5, 6] # 전역 변수에 새로운 객체를 할당
		```


	

5. list append 시 메모리 재할당 발생
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
12. 