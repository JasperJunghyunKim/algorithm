### 개념

* 모든 경우의 수를 체계적으로 탐색하는 알고리즘 중 하나로, [완전탐색](wip%20ExhaustiveSearch.md) 유형의 알고리즘에 속함
* Recursive 방법으로 [DFS](DFS.md) 처럼 구현하나, 탐색 과정에서 Pruning(가지치기)를 적용하여 효율적인 방법으로 문제를 해결하기 위해 사용됨


---
### 구현_Recursive

1. 재귀 함수의 탈출 조건을 설정
   예) visited List 의 길이가 n 에 달했을 때, 합산한 후 return
2. 다음 노드를 탐색하는 조건은 DFS 재귀 알고리즘과 동일하게 구현 (문제마다 조건은 당연히 다름)
3. 다음 노드의 조건을 만족할 때, 다음 노드의 재귀를 실행하기 전후로 **visited 체크 / 체크 해제**

```Python
def recursive(cur_row, cur_col):

	# Pruning 조건
	if len_visited == 4:
		tmp_max = 0
		for r, c in visited:
			tmp_max += number_map[r][c]
		cur_max = tmp_max if tmp_max > cur_max else cur_max
		return

	# 다음 노드 탐색
	for d_r, d_c in [(0,1), (0,-1), (1,0), (-1,0)]:
		next_row, next_col = cur_row + d_r, cur_col + d_c
		if (next_row, next_col) not in visited and 0 <= next_row < NUM_ROW and 0 <= next_col < NUM_COL:
			# 다음 노드 재귀 전후로 visited 체크 / 해제
			visited[len_visited] = (next_row, next_col)
			len_visited += 1
			recursive(next_row, next_col)
			len_visited -= 1
			visited[len_visited] = (-1, -1)
```


---
### 유형

1. 가능한 (순열, 암호 등) 을 모두 구하는 문제
2. 가능한 경우의 수를 모두 구하는 문제
3. [순열, 조합](Combinations%20and%20Permuations.md) - M 과 N (1 ~ 8) 문제
4. N Queen
5. 스토쿠
6. 테트로미노


---
### ⚠️ 주의

### 참고

### 정리중