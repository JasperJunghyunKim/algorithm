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
	   * 이때, I 번째란, 아이템의 정렬 순서가 정해져 있는 것이 아님
	   * for .. I 반복문을 도는 것은 I 개의 아이템을 순회해하며 최적해를 비교해야되기 때문
	   * 즉, 아이템의 정렬 순서는 최종적인 최적해와 관련이 없음 (찾는 과정만 달라질 뿐)
   2. 2차원 배열

---
### 구현 01 Knapsack Problem (item 중복 없는 2차원 배열)

* 각 아이템이 1개만 있는 조건에서, 2차원 DP 배열로 해결
* DP\[C\]\[I\] : 제한 무게가 C  일 때, I 번째 아이템을 선택할 때의 최적해
* [DP](DP.md) 알고리즘에 해당
```python
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


### 구현 - 01 Knapsack Problem (item 중복 없는 1차원 배열)

* 위와 동일한 조건이지만, 1차원 배열을 사용하여 해결
* dp\[w\]
  가용중량이 w 일 때, 얻을 수 있는 최대 가치를 의미
* 역순으로 반복하는 이유는, 현재 아이템을 고려할 때 이전에 계산된 DP 값을 덮어쓰지 않기 위함
* 즉, 각 아이템을 정확히 한 번만 고려하기 위해, 먼저 더 큰 무게에서 더 작은 무게로 이동하면서 각각의 경우에 대해 최대 가치를 계산
* 위는 공간 복잡도가 O(M * N) 이지만, 이건 공간 복잡도가 O(N) 
* [블로그 참조](https://sdy-study.tistory.com/240)
```python
# items : (weight, value) 튜플로 구성된 리스트
dp = [0] * (NUM_ITEMS)

for w, v in items:
	for c in range(MAX_CAPA, -1, -1): # 역순으로 실행
		dp[c] = max(dp[c], v + dp[c - w])
```


### 구현 - 01 Knapsack Problem (item 중복 가능한 경우)

* [[#구현 - 01 Knapsack Problem (item 중복 없는 2차원 배열)]] 를 풀면서, i 번째를 선택할 때의 최적해라고 생각했음
  즉, 물건을 선택하는 순서가 정해져있고, 순서가 바뀔 경우에 답이 달라질 것이라 생각함
  그러나 이 점화식은 **배낭의 가용 중량이 W 일 때, 넣을 수 있는 최대 무게**가 핵심이지, i 순서를 고려한 것은 2 차원 배열에서 Bottom Up 방식으로 해결하기 위한 방법에 불과한 것 이었음
  따라서 item 의 weight, value 입력 순서를 섞어도 결과는 동일하게 나옴
  이 점을 잘 상기해서 아래 내용을 읽을 것
* 이 문제는 각 아이템을 중복으로 선택 가능하다는 조건이 추가된 변형 문제임
* 아이템 전체 개수 N를 줄여서, 전체 시간 복잡도를 log(N) 으로 줄이는 것이 핵심
* 아래와 같이 물건의 무게, 가치, 물건의 중복 개수가 있다고 가정
  (3,3,7), (4,2,4), (1,1,3)
* 이 인풋을 중복 불가한 각각의 아이템으로 변환하면 아래와 같아짐
  (3,3,1), (3,3,1), (3,3,1), (3,3,1), (3,3,1), (3,3,1), (3,3,1), (4,2,1), (4,2,1), (4,2,1), (4,2,1), (1,1,1), (1,1,1), (1,1,1)
* 시간복잡도는 O(NM) 이므로, 기하급수적으로 증가하게 됨
* 각 아이템의 중복 개수를 2진법으로 변환하면, 해당 아이템을 고르지 않는 경우부터, 모두 고르는 경우까지 고려할 수 있으며, 아래와 같이 줄일 수 있음
  (3,3,1), (6,6,1), (12,12,1), (4,2,1), (8,4,1), (4,2,1), (1,1,1), (2,2,1)
* 시간복잡도를 O(logN M) 으로 줄일 수 있음
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
dp = [0] * (M + 1)

# DP를 이용한 최대 가치 계산 
# 1차원 배열 활용
for weight, value in items: 
	for w in range(M, weight - 1, -1): 
	dp[w] = max(dp[w], dp[w - weight] + value)
```



### 향상된 DP (Dictionary 사용 방법)

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

	promising = {0:0}

	for item_w, item_v in items:
		temp = {} # 나중에 promising 에 업데이트 할 임시 딕셔너리 
		for promising_v, promising_w in promising.items():
			new_v = promising_v + item_v
			new_w = promising_w + item_w
			# 새로 계산된 무게(new_w)는 MAX_CAPA 보다 작아야 promising 에 추가할 수 있음
			# 기존에 없던 가치(new_v)라면 promising 에 추가
			# 기존에 있던 가치(new_v)라도 기존 무게보다 작으면 업데아트
			if new_w <= MAX_CAPA and (new_v not in promising or promising[new_v] > new_w):
				temp[new_v] = new_w
		promising.update(temp)

	print(max(promising.keys()))
```


---
### 유형

* 다음과 같이 응용될 수 있음
	1. 최대 무게 M 인 배낭과, 각 W, V 의 무게와 가치를 가진 아이템이 있을 때, 아이템을 선택하여 최대 가치를 만드는 문제
	2. (1) 번에서 각 아이템을 중복으로 여러개 선택할 수 있다는 조건이 추가된 문제
	3. 제한된 N 일(Days)에 대해서, 특정일 마다 시작되는 각 D, P 의 미팅시간과 가치를 가진 미팅이 있을 때, 실행한 미팅의 최대 가지를 만드는 문제
	4. 제한된 T 원의 투자금에 대해서, 각 회사마다 I 원 투자로 V 를 회수할 수 있을 때, 여러 회사에 분산 투자하여 최대 투자금을 회수할 수 있는 문제
	5. (1) ~ (4) 에 대하여 최대 가치를 만들 수 있는 아이템 선택 조합도 함께 출력하는 문제

### 참고
* [블로그](https://howudong.tistory.com/106#article-1--%EB%B0%B0%EB%82%AD-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%9D%B4%EB%9E%80?)
### 정리중