### 개념

* 모든 경우의 수를 체계적으로 탐색하는 알고리즘 중 하나로, [완전탐색](wip%20ExhaustiveSearch.md) 유형의 알고리즘에 속함
* Recursive 방법으로 [DFS](DFS.md) 처럼 구현하나, 탐색 과정에서 Pruning(가지치기)를 적용하여 효율적인 방법으로 문제를 해결하기 위해 사용됨
* Pruning 할 때, Promising(유망한) 노드인지를 체크해야되는데, Promising 을 체크하는 범위를 잘 설정 


### ⚠️ 주의 ⚠️

* Pruning(가지치기) 조건에 따라 시간복잡도 차이가 매우 크게 차이남
  예) N-Queen 문제에서 재귀함수는 Row By Row 실행하므로, Promising 을 체크할 때 
* Promising(유망한) 노드인지를 체크할 때, Promising 체크 범위를 최대한 좁게 설정할 것 → 범위가 넓어지면 결국 시간복잡도가 증가함
* visited 체크하는 방법
  예) N-Queen 


---
### 구현

1. 재귀 함수의 return 조건을 설정
   return 조건은, 탐색 과정에서 경우의 수를 Pruning 하여, 이 값이 Promising 한 것을 의미
   즉, 해가 될 수 있으므로 그 다음 로직을 실행하고 함수 return 
   예) visited List 의 길이가 n 에 달했을 때, 특정 함수를 실행하거나, max 값을 갱신 후 함수 return
2. 다음 노드를 탐색하는 조건은 DFS 재귀 알고리즘과 동일하게 구현 (문제마다 조건은 당연히 다름)
3. 다음 노드의 조건을 만족할 때, 다음 노드의 재귀를 실행하기 전후로 **visited 체크 / 체크 해제**

```Python
# N-Queen 문제
# ROW by ROW 로 백트래킹 함수를 실행
def backtrack(r):
	global num_available
	if r == N:
		num_available += 1
		return
	for c in range(N):
		# COL 중복 제거
		if queen[c] >= 0: continue
		# 대각선 중복 제거
		for dc in range(N):
		# dr = queen[dc]
			if queen[dc] == -1: continue
			# 우상 대각선
			if queen[dc] + dc == r + c:
				break
			# 좌상 대각선
			if queen[dc] - dc == r - c:
				break
		else:
			queen[c] = r # visited check
			backtrack(r + 1) # 재귀 실행
			queen[c] = -1 # 재귀 실행 후, visited check 해제
```


---
### 유형

1. [N Queen](https://www.acmicpc.net/problem/9663)
	* Backtracking 대표적인 문제
	* Pruning 조건 매우 중요
	* 1차원 배열만으로 visited 체크하여, 시간복잡도를 줄임
	* 대각선 확인 방법 주의
2. [순열, 조합](Permutations_and_Combinations.md) - M 과 N (1 ~ 8) 문제
4. 스토쿠
5. 테트로미노


---
### ⚠️ 주의

### 참고

### 정리중