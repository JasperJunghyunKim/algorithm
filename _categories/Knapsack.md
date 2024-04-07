### 개념

* Knapsack Problem
* 담을 수 있는 최대 무게가 정해진 배낭과 각각의 무게와 가치가 주어진 아이템 집합이 있을 때, 배낭에 담은 아이템의 가치의 합이 최대가 되도록 하는 아이템의 조합(부분집합)을 찾는 문제
  (변형된 문제에선, 전체 N 시간에 대해서, 매 시간마다 주어진 미팅의 지속 시간과 미팅 비용이 주어질 때, 전체 N  시간 동안 미팅 비용을 최대로 할 수 있는 미팅들의 조합(부분집합)을 찾는 문제)
* 이는 아이템을 분할할 수 있는지에 따라, Fractional Knapsack Problem, 0-1 Knapsack Problem 으로 구분됨


---
### 구현 - Fractional Knapsack Problem

* 아이템을 분할할 수 있으므로 무게 대비 가치가 가장 높은 아이템 기준으로 정렬하여, 배낭이 꽉 찰 때까지 채우면 됨
* [Greedy](./Greedy.md) 알고리즘에 해당


---
### 구현 - 0 1 Knapsack Problem

* i 번째 아이템(또는 미팅)에 대하여 가방의 가용 중량(또는 가용 미팅시간) 이 k 일 때의 최적해를 DP\[i\]\[k\] 로 표현
* [Dynamic Programming](./DP.md) 알고리즘에 해당


---
### 유형
* 



### ⚠️ 주의

### 참고

### 정리중



* 두 가지 유형이 있음 
	* 분할 가능 냅색
	* 0-1 냅색
	* https://namu.wiki/w/%EB%B0%B0%EB%82%AD%20%EB%AC%B8%EC%A0%9C#s-2
* https://howudong.tistory.com/106