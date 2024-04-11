### 개념

* 대부분의 시험에서는 itertools 라이브러리 사용이 불가함
* 따라서 [Back Tracking](./BackTracking.md) 을 사용하여 직접 구현 필요


### ⚠️ 주의 ⚠️

* 조합을 생성하는 BackTracking 함수를 예로, boolean list 체크 방식과 새로운 리스트에 아이템을 직접 추가하는 방식이 있음
* 이때, 조합을 만드는 것은 boolean list 방식이 빠름
  (매 재귀마다 아이템을 추가하는 Overhead 가 없으므로)
* 단, 실제 조합 리스트를 추출하기까진 후자 방식이 빠름
  (boolean list 방식은, check 여부를 판단하여 리스트를 만들어 내는 오버헤드가 존재하기 때문)
  즉, O(N) 이 더 소요됨
	``` python
	import time
	numbers = [i for i in range(1, 21)]
	number_check = [False for _ in range(20)]
	LEN_NUMBERS = len(numbers)

	def combination(cnt, r, idx):
		global g_cnt
		global g_test_summation
		if cnt == r:
			for i in range(LEN_NUMBERS):
				if number_check[i]: g_test_summation += numbers[i]
			g_cnt += 1
			return
	for i in range(idx, LEN_NUMBERS):
		number_check[i] = True
		combination(cnt + 1, r, i + 1)
		number_check[i] = False

	def combination2(l, cnt, r, idx):
		global g_cnt
		global g_test_summation
		if cnt == r:
			g_cnt += 1
			return
		for i in range(idx, LEN_NUMBERS):
			combination2(l + [numbers[i]], cnt + 1, r, i + 1)

	def combination3(l, cnt, r, idx):
		global g_cnt
		global g_test_summation
		if cnt == r:
			g_cnt += 1
			return
		for i in range(idx, LEN_NUMBERS):
			nl = l[::]
			nl.append(numbers[i])
			combination3(nl, cnt + 1, r, i + 1)

	# 시간 측정
	g_cnt = 1
	g_test_summation = 0
	start_time = time.time()
	combination(0, 9, 0)
	print("combination 1 : Using Boolean Check List")
	print(g_test_summation)
	print(g_cnt)
	print(time.time() - start_time)
	
	g_cnt = 1
	g_test_summation = 0
	start_time = time.time()
	combination2([], 0, 9, 0)
	print("combination 2 : By adding an item directly to new list")
	print(g_test_summation)
	print(g_cnt)
	print(time.time() - start_time)
	
	g_cnt = 1
	g_test_summation = 0
	start_time = time.time()
	combination3([], 0, 9, 0)
	print("combination 3 : By adding an item using append method to new list")
	print(g_test_summation)
	print(g_cnt)
	print(time.time() - start_time)
	```
---
### 구현 - 순열(Permutations)

* 유일하게 visited 배열이 있음 (순서를 고려해야 되므로)
* 재귀 호출 시 list parameter 는 새로운 배열이 되어야하는 점 주의
$$_nP_r = \frac{n!}{(n-r)!}$$

```Python
def permuations(l, length, r):
	global cnt_permutation
	if length == r:
		print(l)
		cnt_permutation += 1
		return
	for i in array:
		if i not in l:
			permuations(l + [i], length + 1, r)

print("PERMUTATIONS")
permuations([], 0, R)
print(cnt_permutation)

######
######

array = [1,2,3,4]
visited = [False] * len(array)

def perm(l, r):
	if len(l) == r:
		print(l)
		return
	for i in range(len(l)):
		if not visited[i]:
			visited[i] = True
			perm(l + [array[i]], r)
			visited[i] = False

perm([], 2) # 12
```


---
### 구현 - 조합(Combinations)

* 이미 선택된 인덱스는 다음 재귀에서 선택하지 않아야 하므로, 파라미터로 인덱스 + 1 을 넘김
$$_nC_r = \frac{n!}{r!(n-r)!}$$

```python
def combination(l, length, r, idx):
	global cnt_combination
	if length == r:
		print(l)
		cnt_combination += 1
		return
	for i in range(idx, len(array)):
		combination(l + [array[i]], length + 1, r, i + 1)

print("COMBINATIONS")
combination([], 0, R, 0)
print(cnt_combination)

######
######

array = [1,2,3,4]

def comb(l, r, idx):
	if len(l) == r:
		print(l)
		return
	for i in range(idx, len(array)):
		comb(l + [array[i]], r, i + 1)

comb([], 2, 0) # 6
```


---
### 구현 - 중복 순열(Product)

* 기존 순열 함수에서, 방문 조건 체크와 백트래킹만 제거하면 됨
* 이미 선택되었더라도, 다음 재귀에서 다시 선택할 수 있음
$$n^2$$

```python
def product(l, length, r):
	global cnt_product
	if length == r:
		print(l)
		cnt_product += 1
		return
	for i in array:
		product(l + [i], length + 1, r)
		
print("PRODUCTS")
product([], 0, R)
print(cnt_product)

######
######

array = [1,2,3,4]

def product(l, r):
	if len(l) == r:
		print(l)
		return
	for i in range(len(array)):
		# if not visited[i]: 
			# visited[i] = True
			product(l + [array[i]], r)
			# visited[i] = False

product([], 2) # 16
```


---
### 구현 - 중복 조합(Multiset Coefficient)

* 기존 조합 함수에서, 다음 재귀함수 인자에 인덱스를 유지하면 됨 (즉, +1 을 하지 않음)
$$_nH_r = _{n+r-1}C_{r}$$
```python
def multiset_coefficient(l, length, r, idx):
	global cnt_multi_coefficient	
	if length == r:	
		print(l)		
		cnt_multi_coefficient += 1		
		return

for i in range(idx, len(array)):
	multiset_coefficient(l + [array[i]], length + 1, r, i)

print("MULTISET COEFFICIENT")
multiset_coefficient([], 0, R, 0)
print(cnt_multi_coefficient)

######
######

arr = [1,2,3,4]

def multiset(new_arr, c, i):
	if len(new_arr) == c:
		print(new_arr)
		return
	for i in range(i, len(arr)):
		multiset(new_arr + [arr[i]], c, i)

multiset([], 2, 0) # 10
```