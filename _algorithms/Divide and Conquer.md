### 개념

* Divide and Conquer (분할 정복)
* 문제를 더 작은 부분 문제로 분할하여 해결한 뒤, 부분 문제의 결과를 결합하여 전체 문제의 결과를 얻는 방법
* 재귀적으로 문제를 해결하며, 세 단계로 나누어 설계함
	1. 분할 (Divide)
	   주어진 문제를 두 개 이상의 부분문제로 나눔
	   이 부분 문제들은 기존 문제와 성격이 동일하고, 규모는 작음
	   예) N * N 행렬을 → (N / 2) * (N / 2) 행렬 4개로 나눔
	   
	2. 정복 (Conquer)
	   부분 문제가 충분히 작아 직접해결할 수 있으면 해결하고, 그렇지 않으면 재귀적으로 다시 분할 정복 알고리즘을 적용
	   
	3. 결합 (Combine)
	   분할된 부분문제의 해결책(Conquer 된 결과)을 결합하여 원래 문제의 해결책을 찾음
* 주어진 문제를 부분 문제로 분할하여 재귀적으로 접근하는 점에서, [DP](./DP.md) 의 TopDown 접근 방법과 유사한 면이 있음


---
### 구현

**Merge Sort**
```python
def merge_sort(arr):
	if len(arr) <= 1: 
		return arr 
		
	# Divide
	mid = len(arr) // 2 
	left_half = merge_sort(arr[:mid]) 
	right_half = merge_sort(arr[mid:]) 
	
	# Conquer
	return merge(left_half, right_half) 
	
def merge(left, right): 
	sorted_arr = [] 
	left_index, right_index = 0, 0 
	
	# 두 하위 배열을 비교하며 하나의 정렬된 배열로 병합합니다. 
	while left_index < len(left) and right_index < len(right): 
		if left[left_index] < right[right_index]:
			sorted_arr.append(left[left_index]) 
			left_index += 1 
		else: 
			sorted_arr.append(right[right_index]) 
			right_index += 1 
	
	# 남은 요소를 결과 배열에 추가합니다. 
	sorted_arr.extend(left[left_index:]) 
	sorted_arr.extend(right[right_index:]) 
	return sorted_arr
```

---
### 유형

* Merge Sort
* Quick Sort
* Binary Sort


---
### Divide and Conquer 와 DP TopDown 차이

* Memoization 여부에 차이가 있음
* DP 는 중복되고, 반복되는 부분 문제를 재활용하기 위해 Memoization 을 하지만, Divde and Conquer 는 각 문제가 독립적이고 중복되지 않는 경우이기 때문에 Memoization 을 하지 않음 


---
### ⚠️ 주의

### 참고

### 정리중