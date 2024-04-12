### 개념

* Knapsack Problem
* 이는 아이템을 분할할 수 있는지에 따라, Fractional Knapsack Problem, 0-1 Knapsack Problem 으로 구분되며, 여기선 [DP](./DP.md) 알고리즘의 한 종류인 0-1 Knapsack 에 대한 설명을 함
* 정의 : 제한된 범위에 대해서, 각 요소를 선택했을 때 최대 가치를 뽑는 문제
* 다음과 같이 응용될 수 있음
	1. 최대 무게 M 인 배낭과, 각 W, V 의 무게와 가치를 가진 아이템이 있을 때, 아이템을 선택하여 최대 가치를 만드는 문제
	2. (1) 번에서 각 아이템을 중복으로 여러개 선택할 수 있다는 조건이 추가된 문제
	3. 제한된 N 일(Days)에 대해서, 특정일 마다 시작되는 각 D, P 의 미팅시간과 가치를 가진 미팅이 있을 때, 실행한 미팅의 최대 가지를 만드는 문제
	4. 제한된 T 원의 투자금에 대해서, 각 회사마다 I 원 투자로 V 를 회수할 수 있을 때, 여러 회사에 분산 투자하여 최대 투자금을 회수할 수 있는 문제
	5. (1) ~ (4) 에 대하여 최대 가치를 만들 수 있는 아이템 선택 조합도 함께 출력하는 문제


### ⚠️ 주의

* ~~일반적으로 다음과 같이 2차원 배열로 해결하는데,
  DP\[i\]\[w\] : 배낭의 무게가 w 일 때 i 번째 아이템을 선택할 때 최대 가치
  이때 item 의 배치 순서는 상관 없음~~

---
### 구현 Fractional Knapsack Problem

* 아이템을 분할할 수 있으므로 무게 대비 가치가 가장 높은 아이템 기준으로 정렬하여, 배낭이 꽉 찰 때까지 채우면 됨
* [Greedy](Greedy.md) 알고리즘에 해당


### 구현 01 Knapsack Problem (item 중복 없는 2차원 배열)

* 각 아이템이 1개만 있는 조건에서, 이를 2차원 DP 배열을 사용하여 해결하는 문제
* dp\[i\]\[w\]
  가용중량이 w 일 때, i 째 아이템까지 고려했을 때의 최적해를 의미
* [Dynamic Programming](DP.md) 알고리즘에 해당
```python
	dp = [[0 for _ in range(MAX_CAPA + 1)] for _ in range(NUM_ITEMS)]

	for capa in range(MAX_CAPA + 1):
		dp[0][capa] = items[0][1] if capa >= items[0][0] else 0

	for i in range(1, NUM_ITEMS):
		for capa in range(MAX_CAPA + 1):
			if capa >= items[i][0]:
				dp[i][capa] = max(dp[i-1][capa], items[i][1] + dp[i-1][capa - items[i][0]])
			else:
				dp[i][capa] = dp[i-1][capa]
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


---
### 유형

### 참고
* [블로그](https://howudong.tistory.com/106#article-1--%EB%B0%B0%EB%82%AD-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%9D%B4%EB%9E%80?)
### 정리중