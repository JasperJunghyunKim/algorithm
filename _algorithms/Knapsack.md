### 개념

* Knapsack Problem 
* 아이템을 분할할 수 있는지에 따라, Fractional Knapsack Problem, 0-1 Knapsack Problem 으로 구분됨
	* Fractional Knapsack 은  [Greedy](Greedy.md)  알고리즘의 한 종류 (무게 대비 가치가 높은 기준으로 정렬 후, 제한 범위에 맞게 아이템을 선택하는 단순한 알고리즘)
	* 01 Knapsack 은 [DP](./DP.md) 알고리즘의 한 종류
* 본 페이지는 01 Knapsack 에 대한 설명을 다룸
* 제한된 범위에 대해서, 각 요소를 선택했을 때 최대 가치를 뽑는 문제
* 다음과 같은 유형과 해결 방법으로 구분할 수 있음
	1. 2차원 DP 배열로 Bottom Up 접근
	2. 1차원 DP 배열로 Bottom Up 접근
	3. 아이템 중복 선택이 가능한 경우
	4. 향상된 DP 구현 (딕셔너리를 사용하는 방법)
	5. 최적해를 도출했을 때, (그 조합에) 어떤 아이템이 선택되었는지 함께 출력

### ⚠️ 주의

1.  1차원 또는 2차원 DP 배열로 접근할 때, 일반적으로 DP\[C\]\[I\] 는 제한 무게가 C  일 때, I 번째 아이템을 선택할 때의 최적해로 정의함
	   * 이때, I 번째란, 아이템의 정렬 순서가 '정해져 있는 것이 아님'
	   * for .. I 반복문을 도는 것은 I 개의 아이템을 순회해하며 최적해를 비교해야되기 때문
	   * 즉, 아이템의 정렬 순서는 최종적인 최적해와 관련이 없음 (찾는 과정만 달라질 뿐)
   2. 1차원 배열로 해결할 때, CAPA 순회는 역순

---
### 구현 01 Knapsack Problem (item 중복 없는 2차원 배열)

* 각 아이템이 1개만 있는 조건에서, 2차원 DP 배열로 해결
* DP\[C\]\[I\] : 제한 무게가 C  일 때, I 번째 아이템을 선택할 때의 최적해
* [DP](DP.md) 알고리즘에 해당
```python
items = [...] # (weight, value)
dp = [[0] * NUM_ITEMS] * (MAX_CAPA + 1)

# 0 번째 아이템 초기화
for c in range(MAX_CAPA + 1):
	dp[c][0] = items[0][value] if c >= items[0][weight] else 0

# 1 번째 아이템부터 마지막까지
for i in range(1, NUM_ITEMS):
	for c in range(MAX_CAPA + 1):
		if items[i][weight] <= c:
			dp[c][i] = max(dp[c][i-1], items[i][value] + dp[c - items[i][weight]][i-1])
		else:
			dp[c][i] = dp[c][i-1]
```


### 구현 01 Knapsack Problem (item 중복 없는 1차원 배열)

* 위와 동일한 조건이지만, 1차원 배열을 사용하여 해결
* DP\[C\] : 제한 무게 C 일 때 최적해
	* 2차원 배열을 구현하면 공간 복잡도가 O(C * I) 소요되는 걸 → O(C) 로 해결하기 위함
* 각 아이템에 대하여, 제한무게 C 를 순회하며 값을 업데이트
* 단!!, C 를 역순으로 순회
	* 현재 아이템을 고려할 때 이전에 계산된 DP 값을 덮어쓰지 않기 위함
	* 기본적으로 DP\[C\] 는 이전 아이템의 DP\[C - k\] 를 참조해야되는데, 오름차순으로 순회할 경우 현재 아이템의 인덱스를 참조하게 되므로
* [블로그 참조](https://sdy-study.tistory.com/240)
```python
items = [...] # (weight, value)
dp = [0] * (MAX_CAPA + 1)

for weight, value in items:
	for c in range(MAX_CAPA, -1, -1): # 역순으로 실행
		dp[c] = max(dp[c], value + dp[c - weight])

# 더 최적화 시키면 아래와 같음
for weight, value in items:
	for c in range(MAX_CAPA, weight - 1, -1): # 역순으로 실행
		dp[c] = max(dp[c], value + dp[c - weight])

```


### 구현 01 Knapsack Problem (item 중복 가능한 경우)

* 각 아이템을 여러개 선택할 수 있다는 조건이 추가된 문제 유형 (각 아이템을 중복으로 선택하는 것이 아님)
* 각 아이템 마다 선택하는 갯수를 2 진법으로 표현하여, O(CN) 을 O(ClogN) 으로 줄이는 것이 핵심
	* C 는 제한 무게
	* N 은 모든 아이템을 1 개짜리로 나열했을 때 전체 개수 (즉, 아이템의 전체 개수)
* 예제)
	* 각 종류의 아이템을 아래와 같이 무게, 가치, 개수로 표시
		* `items = [(3,3,7), (4,2,4), (1,1,3)]`
	* 이걸 각 1개 짜리 아이템으로 변환하면 아래와 같음
		* `items = [(3,3,1), (3,3,1), (3,3,1), (3,3,1), (3,3,1), (3,3,1), (3,3,1), (4,2,1), (4,2,1), (4,2,1), (4,2,1), (1,1,1), (1,1,1), (1,1,1)]`
	* 이 상태로 Knapsack 을 실행해도 되지만, 아이템의 전체 개수가 N 으로 증가했기 때문에, 총 소요 시간은 O(CN) 이 되므로 시간이 오래 걸림
	* 각 종류의 아이템의 선택 방법을 2진법으로 표시하면 아래와 같이 줄일 수 있음
		*  `items = [(3,3,1), (6,6,1), (12,12,1), (4,2,1), (8,4,1), (4,2,1), (1,1,1), (2,2,1)`
		* 특정 종류의 아이템이 9개 있다면, 1개, 2개, 4개, 2개 짜리의 묶음으로 표시할 수 있음
		* 묶음의 크기만큼 무게와 가치는 배가 됨
```python  
for _ in range(N): 
	weight, value, K = map(int, sys.stdin.readline().split()) # 각 물품의 정보 
	
	# 중복 선택한 아이템을 2진법으로 분할
	cnt = 1 
	while K > 0: 
		num = min(K, cnt) 
		items.append((weight * num, value * num)) 
		K -= num 
		cnt *= 2 
# DP 테이블 초기화 
dp = [0] * (MAX_CAPA + 1)

# DP를 이용한 최대 가치 계산 
# 1차원 배열 활용
for weight, value in items: 
	for c in range(MAX_CAPA, weight - 1, -1): 
	dp[c] = max(dp[c], dp[c - weight] + value)
```


### 향상된 DP (Dictionary 사용 방법)

* ⚠️ 아이템의 종류가 많을 경우, DP 배열을 사용하는 방법보다 느려질 수 있음
	* 딕셔너리를 업데이트 하는 비용이 `O(N)` 소요되기 때문
* item 을 물건의 무게 기준으로 내림차순 정렬
* `promising` 이라는 dictionary 를 특정 가치(value)를 만들 수 있는 최소 무게(weight) 로 정의
	* 가치(value) 가 key 가 되며, 무게(weight) 가 value 가 됨
	* 이때 value 는 '가치' 를 의미하는 것이지, 값이 아니므로 혼동하지 말 것
* 딕셔너리 초기값을 {0:0} 으로 초기화
	* 각 아이템을 순회하기 전에는 가치 0 으로 만들 수 있는 무게가 0 임을 의미
* 각 아이템의 가치와 무게에 대하여, 현재 promising 에 담긴 가치와 무게에 값을 더함
	* 기존에 가방에 없던 가치라면 temp 에 추가
	* 기존에 있던 가치라도, 더 작은 무게로 달성할 수 있으면 temp 에 추가
	* 단, 이때 더해진 가치는 최대 무게(MAX_CAPA) 보다 작아야 함
* 각 아이템에 대하여, promising 을 순회했으면, temp 딕셔너리를 기존 promising 에 업데이트

```python
items = [...] # (weight, value)
items.sort(reverse = True)

backpack = {0:0}

for item_w, item_v in items:
	temp_backpack = {} # 나중에 promising 에 업데이트 할 임시 딕셔너리 
	for backpack_v, backpack_w in promising.items():
		new_v = backpack_v + item_v
		new_w = backpack_w + item_w
		# 새로 계산된 무게(new_w)는 MAX_CAPA 보다 작아야 backpack 에 추가할 수 있음
		# 기존에 없던 가치(new_v)라면 backpack 에 추가
		# 기존에 있던 가치(new_v)라도 기존 무게보다 작으면 업데아트
		if new_w <= MAX_CAPA and (new_v not in backpack or backpack[new_v] > new_w):
			temp_backpack[new_v] = new_w
	backpack.update(temp_backpack)

print(max(promising.keys()))
```


---
### 유형

1. 최대 무게 M 인 배낭과, 각 W, V 의 무게와 가치를 가진 아이템이 있을 때, 아이템을 선택하여 최대 가치를 만드는 문제
2. (1) 번에서 각 아이템을 중복으로 여러개 선택할 수 있다는 조건이 추가된 문제
3. 제한된 N 일(Days)에 대해서, 특정일 마다 시작되는 각 D, P 의 미팅시간과 가치를 가진 미팅이 있을 때, 실행한 미팅의 최대 가지를 만드는 문제
4. 제한된 T 원의 투자금에 대해서, 각 회사마다 I 원 투자로 V 를 회수할 수 있을 때, 여러 회사에 분산 투자하여 최대 투자금을 회수할 수 있는 문제
5. (1) ~ (4) 에 대하여 최대 가치를 만들 수 있는 아이템 선택 조합도 함께 출력하는 문제


----
### 참고
* [블로그](https://howudong.tistory.com/106#article-1--%EB%B0%B0%EB%82%AD-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%9D%B4%EB%9E%80?)
### 정리중