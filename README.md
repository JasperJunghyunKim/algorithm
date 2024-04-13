## \[WIP\]시간복잡도, 공간복잡도 (Python3 기준)

**Big-O Notation**
* [빅오 표기법을 설명하다 - 시간과 공간의 복잡도](https://www.freecodecamp.org/korean/news/big-o-notation-why-it-matters-and-why-it-doesnt-1674cfa8a23c/)
* [Complexity Cheat Sheet](https://www.bigocheatsheet.com/)

**공간 복잡도**
* WIP

**시간 복잡도
* WIP
* [코드의 시간 복잡도 계산하기 MEDIUM](https://medium.com/humanscape-tech/%EC%BD%94%EB%93%9C%EC%9D%98-%EC%8B%9C%EA%B0%84-%EB%B3%B5%EC%9E%A1%EB%8F%84-%EA%B3%84%EC%82%B0%ED%95%98%EA%B8%B0-b67dd8625966)

**메모리 계산**
* 메모리 사용량 계산
* 1 MB = 1024 KB, 1KB = 1024 Bytes → 즉, 1 MB = 1024 ^ 2 Bytes 
  (일반적으로 1000 * 1000 으로 계산)
* 파이썬의 int 자료형은 크기가 고정적이지 않고, 수가 커짐에 따라 크기가 커질 수 있음
  단, 일반적으론 아래와 같음
  int : 4 Byte
  float : 8 Byte
* 128 MB 크기의 int 형 배열
  128 MB = 128 * 1024 * 1024 Bytes = 134,217,728 Bytes
  → 134,217,728 / 4 = 33,554,432 길이의 int 배열
* [Python의 데이터 타입 크기 및 기억 범위](https://ilikemediumrare.tistory.com/5)
* [메모리 계산](https://zoosso.tistory.com/995)

**시간 계산**
* 알고리즘의 실행 속도는 시간복잡도 외에도 영향을 끼치는 속도가 많음
* 단, 일반적으론 Python3 기준으로 1초에 20,000,000 번의 계산으로 전제함
	```python
	import time

	# CASE 1
	# O(N), N = 20_000_000
	time_before = time.time()
	a = 0
	for i in range(20_000_000):
		a += i
	print("DURATION : ", time.time() - time_before) # 1.191xxxx
	print(a)
	
	  
	# CASE 2
	# O(N*M), N = 50_000, M = 400, N * M = 20_000_000
	time_before = time.time()	
	a = 0
	for i in range(50_000):
		for j in range(400):
			a += j
	print("DURATION : ", time.time() - time_before) # 1.0750xxx
	print(a)
	```
* 시간 복잡도의 허용 범위 내에서 N 의 최대 크기는 아래 표를 참조하면 안전할 수 있음![timecomplexity.png](./_imgsrc/timecomplexity.png)
* 실제 시험 땐, 각 변수의 최대값을 입력하여 시간을 측정해보는 것까지 포함할 것
* [파이썬 시간 계산](https://wjswhdgur123.tistory.com/74)


---
## Python3, PyPy3 차이

* 일부 문제는 PyPy3 로 실행했을 때만 시간초과 없이 통과됨
* PyPy3 는 무엇이고, Python3 와는 어떤 차이가 있는지 확인

**Python**
* Python 은 기본적으로 인터프리터 언어로 분류
* `.py` 으로 작성된 코드는 바이트 코드인 `.pyc` 파일로 컴파일되는 중간 단계를 거치며, 이 바이트 코드는 Python VM (PVM) 위에서 실행됨
* 컴파일 과정이 있음에도 Python 은 인터프리터 언어로 분류됨
* 대표적으로 두 종류의 인터프리터가 있음 #CPython #PyPy3

**CPython(Python3)**
* Python 언어의 가장 기본적이고 널리 사용되는 구현
* C 는 인터프리터가 C 언어로 작성되었음을 의미
* Python 으로 작성된 대부분의 라이브러라와 프레임워크는 CPython 과 호환됨
* CPython은 Python의 표준 라이브러리와 함께 제공되며, 플랫폼 독립적인 프로그래밍과 확장 모듈을 지원

**PyPy3**
* Python3 코드를 실행하기 위한 대체 인터프리터(Interpreter)
* Just-In-Time(JIT) 컴파일러를 사용하며, 이는 프로그램 실행 중에 코드를 분석하고 자주 실행되는 부분(핫스팟)을 감지하여 기계어로 변환
* 따라서 반복적인 계산이 많거나 장시간 실행되는 스크립트에서 Python3(CPython)보다 뛰어난 성능을 보임
	* 반복문을 통한 계산
	* 재귀 함수 (예. [BackTracking](./algorithms/BackTracking.md))
	* 수학적 계산이 많이 요구되는 경우 (예. [DP](./algorithms/DP.md) 와 같이 값을 계속 갱신해야되는 경우)
* 그러나 일부 경우엔 Python3의 코드와 완벽하게 호환되지 않을 수 있으며, C 확장 모듈과의 호환성이 제한될 수 있음

**결론**
* 둘 다 Python 인터프리터의 일종
* 반복되는 코드가 많을 경우 PyPy3 가 실행 성능이 더 빠를 수 있음
* 단, 실행 코드가 PyPy3 와 호환되지 않을 수 있으므로 유의

**출처**
* [블로그](https://ralp0217.tistory.com/entry/Python3-%EC%99%80-PyPy3-%EC%B0%A8%EC%9D%B4)


-----------
## 문제 구현 (Python)

* 연습 문제 풀면서 헷갈렸던 구현들 또는 구현에 도움되는 내장함수 또는 모듈 정리
  ~~(다시 공부할 때)~~

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

	# 3차원 배열의 경우 아래와 같이
	new_3d = [[j[::] for j in i] for i in old_3d]
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
	
	**기본 자료형 (Primitive Type)**
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
	  (재할당 시 뒷 공간이 충분하다면 그냥 들림)
	* 재할당 과정에서 새로운 주소로 옮길 경우 시간이 많이 소요됨
	* for 문을 통해 많은 양의 데이터를 list 에 추가하는 경우가 이에 해당됨

	**결과 요약**
	* Case 1 의 소요 시간이 압도적으로 높음
	* Case 3 의 append 방식이 생각보다 시간이 오래 소요되지 않았음
	
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

	before = time.time()
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
	* [Permuations and Combinations](Permutations%20and%20Combinations.md)
	
16. 참조형 변수

	* ~~Param 으로 참조형 자료형을 넣고, 그 자료형 자체가 변경되었을 때 리턴되는거~~

17. sort vs sorted, reverse vs reversed

	* 속도는 sort, reverse 가 더 빠름
	* sorted, reversed 는 메모리를 2 배 사용하기 때문

18. 그래프 사이클 찾기
	
	* Union Find, DFS

19. recursion limit
    
	* Python 의 기본 재귀 깊이 제한은 1000 으로, 매우 얕은 편
	* 따라서 재귀를 사용하여 해결할 경우 이를 풀어줘야 함
	* [블로그](https://fuzzysound.github.io/sys-setrecursionlimit)
	```python
	sys.setrecurionlimit(10 ** 6)
	```


---
## 주의사항

1. 중복 제거를 위해선 set 을 사용
2. 냅색 중복 허용되는 문제 → 각 item 을 선택하는 개수의 경우를 2 진법으로 표시 → 그상태로 일반 냅색
3. DP 문제 해결 시(냅색 포함), 아래 조건을 생각할 것
	* i 번째 할 경우, 하지 않을 경우
	* i 번째가 가능한 경우, 물리적으로 불가한 경우
1. 주사위 문제 
	* 주사위, 큐브 두 가지 종류가 있음
	* 주사위 굴림과 회전을 잘 구분할 것
2. 백트래킹 시, 경우의 수가 중복되는지 잘 확인할 것
	* 14502 연구소 문제에서 3 개의 벽을 세우는 '조합' 으로 접근해야되는데, 수열로 접근하여 시간초과
3. 백트래킹 시, 경로를 알아야되는 게 아니라면 collection 을 저장할 필요 없음
	* 14888 연산자 끼워넣기 문제에서 연산자의 순열을 만들어내느라 시간이 오래 걸림 → 연산자의 잔여 개수를 인자로 넘겨주기만 해도 해결 가능
4. 백트래킹 시, 어떤 인자를 넘길 것 인지 주의 → 잘 못 선택하면 시간 낭비
5. 사이클 발생할 경우 몫과 나머지 활용 -> 시간 초과 함정 
6. 나누기 연산 필요 시 zero division error 주의


---
## 공부순서 참고

* [알고리즘 공부 순서 VELOG](https://velog.io/@cxxerry/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B3%B5%EB%B6%80-%EC%88%9C%EC%84%9C)
* [알고리즘 공부 순서 - 문제 정리](https://patiencelee.tistory.com/1072)
* [한 장으로 보는 알고리즘 공부 순서](https://velog.io/@ngngs/%ED%95%9C-%EC%9E%A5%EC%9C%BC%EB%A1%9C-%EB%B3%B4%EB%8A%94-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98)


---
## 학습 전

* 완전탐색 → Meet In the Middle (BOJ 1208, 7453, 1450)
* 벨만포드
* 크루스칼(MST)
* 문자열 알고리즘
  KMP
* 이분탐색
* 트리 지름 계산
* 슬라이딩 윈도우
* 세그먼트 트리
