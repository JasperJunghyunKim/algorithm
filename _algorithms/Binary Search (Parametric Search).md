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
	* `low <= high` 조건 주의 : 같을 때까지 실행하지 않으면(등호를 빼면), target 을 찾을 수 없음
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

1. Parametric Search
	* 최적화 문제를 결정 문제로 바꾸어 해결 하는 것
		* 최적화 문제, 즉, 문제의 상황을 만족하는 최소값(또는 최대값)을 구하는 문제를, 최소값(또는 최대값)일 때 결정하는 문제로 바꾸어 해결
	* 어떤 정보를 바이너리 서치할 것인지를 잘 찾아야 함
		* 예) [입국 심사](https://school.programmers.co.kr/learn/courses/30/lessons/43238) 문제에선, 시간을 기준으로 바이너리 서치를 하여, 그 시간 동안 N 명을 통과시킬 수 있는지 여부로 Up Down 실행
	* 어떠한 타겟을 최소 N 을 만들기 위해, 최대 크기 M 의 수단을 구하는 문제
		* ⚠️ while 을 탈출했을 때, 어떤 값을 리턴하는지 잘 확인할 것
		* 예) [랜선 자르기](https://www.acmicpc.net/problem/1654), [나무 자르기](https://www.acmicpc.net/problem/2805) 
		* 자를 길이를 이분 탐색으로 접근
		* 최소 N 조건을 만족할 경우, `low = mid + 1` 하여 탐색 하한 범위를 늘려서, 더 큰 M 을 찾음
		* 조건을 만족하지 않을 경우, `high = mid - 1` 하여 탐색 상한 범위를 줄여서, 더 작은 M 을 찾음
		* 최대를 찾는 문제이므로 <u>high 값 반환</u>
	* 어떠한 타겟을 최대 N 을 만들기 위해, 최대 크기 M 의 수단을 구하는 문제
		* 예) [입국 심사](https://school.programmers.co.kr/learn/courses/30/lessons/43238)
		* 최소를 찾는 문제이므로 <u>low 값 반환</u>

### E. 참고

### F. 정리중