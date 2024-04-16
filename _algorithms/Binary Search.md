### A. 개념

* <u>정렬된 배열</u>에서 특정한 값을 찾는 검색 알고리즘
* 탐색하려는 범위를 반으로 줄여가며 데이터를 찾는 원리이며, 시작점, 중간점, 끝점을 이용하여 탐색 범위를 조절함
* 구현 순서
	1. 정렬된 배열과 구하려는 값을 찾음
	2. `low`, `high` 인덱스를 정함
	3. `low <= high` 조건에 대해서 (4) ~ (5) 를 실행
		* 즉, `low > high` 가 되면 탈출하고 (6) 을 실행 → 해당 인덱스가 존재하지 않으므로
	4. `mid` 인덱스를 계산 (`mid = (low + high) // 2`) 
	5. `mid` 인덱스와 찾고자하는 값 `target` 을 비교
		* `array[mid] == target`이면, `mid` 인덱스를 리턴
		* `array[mid] < target`이면, `low`를 `mid + 1`로 설정
		* `array[mid] > target`이면, `high`를 `mid - 1`로 설정
	6. (5) 의 `low` > `high` 가 실행되면 `target` 이 배열에 존재하지 않으므로 `-1` 값을 리턴

### B. ⚠️ 주의 ⚠️
### C. 구현

* 시간복잡도
	* 매번 절반으로 탐색 범위를 줄이기 때문
	* 선형탐색 O(N) 보다 시간복잡도를 개선 
	  $$O(log_{2}N)$$
* 반복문
	```python
	def binary_search(array, target):
		low, high = 0, len(array) - 1
		while low <= high:
			mid = (low + high) // 2
			if array[mid] == target:
				return mid
			elif target > array[mid]:
				low = mid + 1
			elif target < array[mid]:
				high = mid - 1
		return -1
	```

* 재귀
	```Python
	def binary_search(array, target, low, high):
		if low > high:
			return -1
		mid = (low + high) // 2
		if array[mid] == target:
			return mid
		elif target > array[mid]:
			return binary_search(array, target, mid + 1, high)
		elif target < array[mid]:
			return binary_seach(array, target, low, mid - 1)
	```


---
### D. Python 라이브러리 - `bisect`

* Python 은 `bisect` 라는 이진 탐색 라이브러리를 지원
* `bisect_left(a, x)`
	* 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메소드
- `bisect_right(a, x)`
	- 정렬된 순서를 유지하도록 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메소드
```python
from bisect import bisect_left, bisect_right
a = [1,2,3,4,5,5,5,5,6,7] # 10개
x = 5

print(bisect_left(a, x)) # 5를 넣을 수 있는 인덱스 중, 가장 왼쪽 : 4
print(bisect_right(a, x)) # 5를 넣을 수 있는 인덱스 중, 가장 오른쪽 : 8
```
* 이를 이용하여 정렬된 리스트에서, 원소의 개수를 구할 수 있음
```python
from bisect import bisect_left, bisect_right
a = [1,2,3,4,5,5,5,5,6,7] # 10개
x = 5

print(biset_right(a,x) - bisect_left(a,x)) # 4 개
```


---
### D. 유형

### E. 참고

### F. 정리중