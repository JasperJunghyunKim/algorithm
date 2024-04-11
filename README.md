

* 


https://garden1500.tistory.com/8
[알고리즘 공부 순서 VELOG](https://velog.io/@cxxerry/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B3%B5%EB%B6%80-%EC%88%9C%EC%84%9C)
[알고리즘 공부 순서 - 문제 정리](https://patiencelee.tistory.com/1072)
[한 장으로 보는 알고리즘 공부 순서](https://velog.io/@ngngs/%ED%95%9C-%EC%9E%A5%EC%9C%BC%EB%A1%9C-%EB%B3%B4%EB%8A%94-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98)


int형은 4바이트입니다.

1KB는 1024바이트입니다.

1MB는 1024KB입니다.

128MB = 128 * 1024KB = 128 * 1024 * 1024B = int형 128 * 1024 * 1024 / 4개 = 33554432개입니다.

사실 1024로 계산하기가 까다로워서, 대충 1000이라고 놓고 계산하면 얼추 맞습니다.


* 자료형 별 메모리 정리

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


## 시험 전







-----------
## 문제 구현 (Python)

* 연습 문제 풀이 시, ⚠️ 자주 발생했던 실수 정리 ⚠️ 
* 구현에 도움되는 내장함수 또는 모듈 정리

1. Deep Copy + Slicing

	* 문제를 풀 때, 컬렉션(특히 리스트)을 복사할 경우가 있음
	* 이때, 단순히 새로운 변수에 대입해버리면 메모리 주소도 복사되어 기존 배열을 건드리는 경우가 있음
	* 따라서 slicing 을 사용하거나, copy 모듈을 사용	
	``` Python
	a = [1,2,3]
	b = a[::]

	import copy
	c = copy.deepcopy(a)
	```

	**⚠️ 2 차원 배열 Deep Copy**
	* 2 차원 배열은, list 안에 list 가 중첩된 구조로, 참조형 자료형이 또 있기 때문에, 단순히 위와 같이 slicing 하면 안됨
	* list 내 각각의 list 에 대하여 slicing 필요
	* ~~[BOJ 14502 연구소](https://www.acmicpc.net/problem/14502) 문제풀면서 틀릴뻔 함~~
	```python
	a = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
	b = [i[::] for i in a]
	```


2. 자료구조 별 Visited Check 성능 비교
	
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

9. list - item 추가 시 속도, 메모리 비교
	
	* 참고
		* [파이썬 메모리 관리 방법](https://yomangstartup.tistory.com/105)
		* [파이썬 속도 개선](https://atelier-house.tistory.com/3)
		* [파이썬 메모리 할당, 해제, 재할당](https://velog.io/@yun9yu/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%A9%94%EB%AA%A8%EB%A6%AC-%ED%95%A0%EB%8B%B9)
	
	**메모리 재할당**
	* 파이썬은 필요한 메모리 양이 바뀔 경우, 다시 메모리를 할당 받음
	  재할당 시 뒷 공간이 충분하다면 그냥 늘리면 되지만, 공간이 없다면 할당 영역을 옮기고 재할당 해야함
	* 따라서 빈번한 메모리 재할당은 새로운 메모리를 할당 받아야하므로 가급적 피하는 것이 좋음
	* for 문을 통해 많은 양의 데이터를 list 에 추가하는 경우가 이에 해당됨
	  Case 5 와 나머지를 비교했을 때, 메모리 사용량이 크게 차이남 
	
	```PYTHON
	import time
	import random
	import psutil
	SIZE = 20_000
	g_mem = 0
	
	# sample_list = [i for i in range(SIZE)]
	sample_list = random.sample(range(SIZE), SIZE)
	
	# memory check
	def mem_usage():
		p = psutil.Process()
		#byte를 사람이 인지하기 쉬운 megabyte로 변환
		#megabyte이므로 1024 * 1024의 값을 나눠줌
		return p.memory_info().rss

	# CASE 1
	# 새 리스트인 [item] 을 case_1 에 더하는 방식으로 case_1 에 할당함
	# 이 과정에서 [item] 이라는 중간 객체가 생성되므로, 메모리 사용량이 급격히 증가함
	def f1():
		global g_mem
		case_1 = []
		start_time = time.time()
		for item in sample_list:
			case_1 = case_1 + [item]
		print("CASE 1 TIME : ", time.time() - start_time)
		print("CASE 1 MEM : ", mem_usage() - g_mem, " BYTES")
		print()

	# CASE 2
	# += 연산자로 [item] 을 in-place 로 추가
	# 메모리 재할당이 발생하지만, 중간 객체가 생성되지 않으으로 CASE1 보다 메모리 효율이 높음
	def f2():
		case_2 = []
		start_time = time.time()
		for item in sample_list:
			case_2 += [item]
		print("CASE 2 TIME : ", time.time() - start_time)
		print("CASE 2 MEM : ", mem_usage() - g_mem, " BYTES")
		print()
	
	  
	
	# CASE 3
	# in-place 로 추가
	# CASE2 와 마찬가지로 재할당만 발생
	def f3():
		case_3 = []
		start_time = time.time()
		for item in sample_list:
			case_3.append(item)
		print("CASE 3 TIME : ", time.time() - start_time)
		print("CASE 3 MEM : ", mem_usage() - g_mem, " BYTES")
		print()

	# CASE 4
	# CASE3 의 append 라는 메서드를 호출하는 오버헤드를 줄이고자 했으나, 겨로가적으로 큰 차이 나지 않음
	# 메모리적으로도 CASE3와 차이나지 않음
	def f4():
		case_4 = []
		start_time = time.time()
		append_to_4 = case_4.append
		for item in sample_list:
			append_to_4(item)
		print("TEST CASE 4 : ", time.time() - start_time)
		print("CASE 4 MEM : ", mem_usage() - g_mem, " BYTES")
		print()

	# CASE 5
	# 미리 큰 메모리를 할당하므로, 재할당은 발생하지 않음
	# 초기 메모리 사용량이 큼
	def f5():
		case_5 = [1 for _ in range(SIZE)]
		start_time = time.time()
		for i, v in enumerate(sample_list):
			case_5[i] = sample_list[i]
		print("TEST CASE 5 : ", time.time() - start_time)
		print("CASE 5 MEM : ", mem_usage() - g_mem, " BYTES")
		print()
	
	g_mem = mem_usage()
	f1()
	g_mem = mem_usage()
	f2()
	g_mem = mem_usage()
	f3()
	g_mem = mem_usage()
	f4()
	g_mem = mem_usage()
	f5()
	```

	```python
	import time

	import random
	
	  
	
	before = time.time()
	
	a = [0] * 1_000_000
	
	print("[0] * N : ", time.time()-before, "s")
	
	print()
	
	  
	
	before = time.time()
	
	a = [0 for _ in range(1_000_000)]
	
	print("0 - COMPREHENSION : ", time.time()-before, "s")
	
	print()
	
	  
	  
	
	for _ in range(1_000_000):
	
	a.append(random.randint(1, 10000))
	
	print("RANDOM APPEND : ", time.time()-before, "s")
	
	print()
	
	  
	
	before = time.time()
	
	a = [random.randint(1, 10000) for _ in range(1_000_000)]
	
	print("RANDOM COMPREHENSION : ", time.time()-before, "s")
	
	print()
	```


10. Lambda 함수 활용

	**Sort**
	```python
	a = [(1,2), (2,4), (2,1), (1,6), (1,3), (3,1), (4,7), (3,5)]

	# 리스트 각 원소의 두 번쨰 인덱스(x[1]) 기준으로 정렬 후, 
	# 첫 번째 인덱스(x[0])으로 정렬
	a.sort(key = lambda x : (x[1], x[0]))
	```

	**Map**
	```python
	a = [1,2,3,4,5]
	a = map(lambda x : x * 2, a) # [2,4,6,8,10]
	```

11. sys.stdin.readline vs input 메서드의 속도 차이

	* 참고
		* [Velog 파이썬 입력 받기](https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline)
	* input 메서드는 내부적으로 stdin(표준 입력)을 입력받기 전 프롬프트를 출력하고, 개행 문자를 제거하는 작업을 수행함
	* 반면 sys.stdin.readline 는 stdin(표준 입력)에서 한 줄을 읽어들이는 것이 전부이며, 개행 문자를 그대로 포함함
	* 특히 입력 받는 데이터 양이 많아지면, input 메서드의 오버헤드가 누적되어, 실행 시간을 크게 증가시킬 수 있음

	```python
	import sys
	sys_input = sys.stdin.readline

	# 입력받은 N 개의 문자를 MAP 으로 정수 변환 후, 리스트로 저장
	a = list(map(int, sys_input().strip().split())) 
	```

12. enumerate

	```python
	l = [a,b,c,d]
	for k, v in enumerate(l):
		print(k ,v) # 0, a / 1, b / 2, c ...

	d = {1:'a',2:'b',3:'c',4:'d',5:'e'}

	for k, v in enumerate(d):
		print(k, v) # 0 ,1 / 1, 2 / 2, 3 ...
	```

13. zip
	
	* 두 개 이상의 iterable 객체에 대하여, 여러 데이터를 병렬로 처리해야 할 때 유용하게 사용됨 
	* 예를 들어, 두 리스트의 같은 위치에 있는 요소들을 동시에 처리하거나, 여러 리스트의 요소들로부터 새로운 데이터 구조를 생성할 때 활용
	* iterable 중 짧은 것을 기준으로 반환
	
	```python
	a = [1, 2, 3]
	b = ['a', 'b', 'c', 'd']
	print(list(zip(a, b))) # [(1, 'a'), (2, 'b'), (3, 'c')]
	```
	
14. iteration 실행 시 dictionary 사이즈 변경 불가

	* RuntimeError: dictionary changed size during iteration
	```python
	a = {1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8}
	
	for k,v in a.items():
		if k % 2 == 0:
		a.pop(k)
	```

15. 순열과 조합

	* 대부분의 시험에서는 itertools 라이브러리 사용이 불가함
	* 따라서 직접 구현할 수 있어야 함
	* [Permuations and Combinations](Permutations_and_Combinations.md)
	
16. 참조형 변수

	* ~~Param 으로 참조형 자료형을 넣고, 그 자료형 자체가 변경되었을 때 리턴되는거~~

2. sort vs sorted, reverse vs reversed

	* 속도는 sort, reverse 가 더 빠름
	* sorted, reversed 는 메모리를 2 배 사용하기 때문

3. itertools - combinations, permutations
4. if (a_r, a_c) == (b_r, b_c) == (c_r, c_c): continue
5. recursion limut
	* https://fuzzysound.github.io/sys-setrecursionlimit
	* 1000 으로 매우 낮음
6. 대각선 상하
	* N Queen 문제*