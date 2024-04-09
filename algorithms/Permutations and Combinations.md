### 개념

* 대부분의 시험에서는 itertools 라이브러리 사용이 불가함
	* itertools 
* 따라서 [Back Tracking](./BackTracking.md) 을 사용하여 직접 구현해야 함


---
### 구현 - 순열(Permutations)

* 유일하게 visited 배열이 있음 (순서를 고려해야 되므로)
* 재귀 호출 시 list parameter 는 새로운 배열이 되어야하는 점 주의
$$_nP_r = \frac{n!}{(n-r)!}$$

```Python
arr = [1,2,3,4]
visited = [False] * len(arr)

def perm(new_arr, c):
	if len(new_arr) == c:
		print(new_arr)
		return
	for i in range(len(arr)):
		if not visited[i]:
			visited[i] = True
			perm(new_arr + [arr[i]], c)
			visited[i] = False

perm([], 2) # 12
```


---
### 구현 - 조합(Combinations)

* 이미 선택된 인덱스는 다음 재귀에서 선택하지 않아야 하므로, 파라미터로 인덱스 + 1 을 넘김
$$_nC_r = \frac{n!}{r!(n-r)!}$$

```python
arr = [1,2,3,4]

def comb(new_arr, c, i):
	if len(new_arr) == c:
		print(new_arr)
		return
	for i in range(i, len(arr)):
		comb(new_arr + [arr[i]], c, i + 1)

comb([], 2, 0) # 6
```


---
### 구현 - 중복 순열(Product)

* 기존 순열 함수에서, 방문 조건 체크와 백트래킹만 제거하면 됨
* 이미 선택되었더라도, 다음 재귀에서 다시 선택할 수 있음
$$n^2$$

```python
arr = [1,2,3,4]

def product(new_arr, c):
	if len(new_arr) == c:
		print(new_arr)
		return
	for i in range(len(arr)):
		# if not visited[i]:  // 제거
			# visited[i] = True // 제거
			product(new_arr + [arr[i]], c)
			# visited[i] = False // 제거

product([], 2) # 16
```


---
### 구현 - 중복 조합(Multiset Coefficient)

* 기존 조합 함수에서, 다음 재귀함수 인자에 인덱스를 유지하면 됨 (즉, +1 을 하지 않음)
$$_nH_r = _{n+r-1}C_{r}$$
```python
arr = [1,2,3,4]

def multiset(new_arr, c, i):
	if len(new_arr) == c:
		print(new_arr)
		return
	for i in range(i, len(arr)):
		multiset(new_arr + [arr[i]], c, i)

multiset([], 2, 0) # 10
```