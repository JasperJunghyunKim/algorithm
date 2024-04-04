


https://garden1500.tistory.com/8
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

	# 전역 변수의 내용을 변경하므로 global 불필요
	def update_list(): 
		my_list.append(4)
		 
	# 전역 변수에 새로운 객체를 할당하므로 global 필요
	def replace_list(): 
		global my_list 
		my_list = [4, 5, 6] 
	```

4. swap
	
	```python
	a = 10, b = 20
	a, b = b, a
	print(a, b) # 20, 10
	```

5. Collection Comprehension (List, Dict, Set, Tuple)
	- 새로운 컬렉션을 만들기 위해 기존 컬렉션을 기반으로 간결하게 표현하는 Python 문법
	- ⚠️ range 는 순차적인 값을 생성하기 위해 사용되며, 기존 컬렉션과는 다름
	  range 는 모든 값을 메모리에 저장하지 않고, 대신, 필요할 때 마다 숫자를 생성하므로 메모리를 절약할 수 있음

	**기본**
	```python
	# [0,1,2,3,4,5]
	list_a = [i for i in range(6)]
	```

	**조건부**
	```python
	list_a = [0,1,2,3,4,5,6,7,8,9]

	# [0,2,4,6,8]
	list_b = [i for i in list_a if i % 2 == 0]
	# [-1,1,-1,3,-1,5,-1,7,-1,9]
	list_c = [i if i % 2 else -1 for i in list_a]
	```

	**Dict Deep Copy**
	```python
	dict_a = {1:[a,b], 2:[c,d], 3:[e,f], 4:[g,h]}
	dict_b = {k:v for k, v in dict_a.items()}
	```

6. Dict 활용

	**추가**
	```python
	a = {1:[1], 2:[2,3]}
	a[3] = [3,4,5]
	```


	**조회**
	* Key 에 직접 접근하거나, get 메서드를 사용할 수 있음
	* 단, Key 에 직접 접근할 경우, 해당 Key 가 없으면 #KeyError 발생
	* get 메서드를 사용하는 경우, Key 가 없을 경우 None 반환하므로 안전
	``` Python
	print(a[2]) # [2,3]

	print(a.get(5)) # None
	```

	**삭제**
	- 삭제하기 위해선 POP 또는 DEL 메서드를 사용할 수 있음
	  POP 은 제거되는 Key 의 Value 를 반환하며, DEL 은 그냥 제거함
	* Key 가 없을 경우, 둘 다 #KeyError 발생
	  단, POP 의 경우 Key 가 없을 경우 Default 값을 지정 가능
	``` Python
	del d[1]
	
	d.pop(100, None)
	```

7. range(N) iterable 역순 출력

	```python
	N = 10
	a = [i for i in range(N)]
	
	# [9,8,7,6,5,4,3,2,1,0]
	b = [i for i in range(N-1, -1, -1)]
	```

8. round(), floor(), ceil()

	**\[주의\] 반올림**
	* 모듈 import 할 필요 없이, 내장 함수를 바로 사용할 수 있음
	* ⚠️ round 는 정수부가 홀수일 경우 올림, 짝수일 경우 내림되어 계산됨
	  따라서 아래 코드와 같이 의도치 않은 결과가 나옴
	* 이는 간단하게 0.5 를 더한 후, 내림 함수를 사용하여 해결할 수 있음
	``` python
	# 예상과 다른 결과가 나옴
	a = [0.5, 1.5, 2.5, 3.5, 4.5]
	for i in a: print(round(i)) # 0, 2, 2, 4, 4

	# floor 로 해결
	b = [0.3, 1.2, 2.7, 3.4, 4.9]
	b = map(lambda x : x + 0.5, b)
	for j in b: print(math.floor(j)) # 0, 1, 3, 3, 5
	```

	**올림, 내림**
	* math 모듈 사용
	``` python
	import math
	print(math.ceil(1.1)) # 2
	print(math.floor(1.9)) # 1
	```



1. list append 시 메모리 재할당 발생
		https://atelier-house.tistory.com/3

1. sys.stdin.readline / input 차이
2. sys.stdout.write / print 차이
3. tuple 로 구성된 list 정렬
	- 정렬 기준 : tuple 의 두 번째 원소 → 첫 번째 원소 순서
``` python
list().sort(key = lambda x : (x[1], x[0]))
```


8. sort vs sorted
9. itertools - combinations, permutations
10. visited 구현
	* x is in list() 대신, boolean list 로 구현
11. enumerate