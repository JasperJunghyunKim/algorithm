### 개념

* 대부분의 시험에서는 itertools 라이브러리 사용이 불가함
* 따라서 [BackTracking](./BackTracking.md) 을 사용하여 직접 구현 필요


### ⚠️ 주의 ⚠️

* BackTracking 을 사용하여 경우의 수를 고려하는 예로, 대표적으로, Visited 리스트를 사용하여 boolean 체크하는 방식과 새로운 리스트 생성하여 다음 재귀 함수의 인자로 넘겨주는 방식이 있음
* 30C15 조합을 계산하는 것을 예로, 각 방식의 속도 비교
* Combination 1 : visited check 사용하는 방식
* Combination 2: 함수 인자로 리스트를 넘겨주되, 리스트에 아이템을 더히기 연산으로 추가하여 새로운 리스트를 넘겨주는 방식
* Combination 3: 함수 인자로 리스트를 넘겨주되, append, pop 방식을 사용

**TEST 1 : 경우의 수만 추출하는 경우**
* 전체 경우의 수만 추출하고, 각 조합 자체는 접근하지 않을 경우
* 실행 시간 : `Comb 1 << Comb3 << Comb2`
* Visited 만 체크하면 되므로 Comb 1 가 압도적으로 빠름
  (하지만 대부분의 문제에선 전체 경우의 수만 추출하는 경우는 잘 없고, 대부분 각 조합 자체를 순회하여 함수를 추가로 돌려야 함)
* 의외로 list 를 직접 append 하고 pop 하는 Case 3 의 방식도 빠름
	```powershell
	COMBINATION 1
	SUM :  0
	CNT :  155117520
	TIME :  57.03505492210388
	
	COMBINATION 2
	SUM :  0
	CNT :  155117520
	TIME :  90.94562983512878
	
	COMBINATION 3
	SUM :  0
	CNT :  155117520
	TIME :  63.16774916648865
	```

 **TEST 2 : 각 경우의 조합 자체에 접근해야되는 경우**
 * `r == 15`  인 각각의 조합에 대하여 어떠한 연산이 필요할 경우
 * 실행 시간 : `Comb 3 << Comb2 << Comb1`
 * Visited 체크 방식은, Length == 15 가 되었을 때, 전체 N 을 순회하여 다시 조합을 생성해야 되므로 속도가 느림 (O(N) 이 더 소요됨) 
	 ```powershell
	 COMBINATION 1
	 SUM :  33738060600
	 CNT :  155117520
	 TIME :  204.64266419410706
	 
	 COMBINATION 2
	 SUM :  33738060600
	 CNT :  155117520
	 TIME :  167.378897190094
	 
	 COMBINATION 3
	 SUM :  33738060600
	 CNT :  155117520
	 TIME :  138.69780707359314
	```


**테스트 코드**
``` python
import time
LEN_NUM = 30
R = 15
numbers = [i for i in range(LEN_NUM)]

g_comb1_sum = 0
g_comb2_sum = 0
g_comb3_sum = 0
g_comb1_cnt = 0
g_comb2_cnt = 0
g_comb3_cnt = 0


# COMBINATION 1
selected = [False] * LEN_NUM
def combination1(length, r, idx):
	global g_comb1_sum
	global g_comb1_cnt
	if length == r:
		g_comb1_cnt += 1
		for i in range(LEN_NUM):
			if selected[i]:
				g_comb1_sum += numbers[i]
		return
	for i in range(idx, LEN_NUM):
		selected[i] = True
		combination1(length + 1, r, i + 1)
		selected[i] = False
  
time_before = time.time()
print("COMBINATION 1")
combination1(0, R, 0)
print("SUM : ", g_comb1_sum)
print("CNT : ", g_comb1_cnt)
print("TIME : ", time.time() - time_before)

  
# COMBINATION 2
def combination2(comb_list, length, r, idx):
	global g_comb2_sum
	global g_comb2_cnt
	if length == r:
		g_comb2_cnt += 1
		for i in comb_list:
			g_comb2_sum += i
		return
	for i in range(idx, LEN_NUM):
	combination2(comb_list + [numbers[i]], length + 1, r, i + 1)

time_before = time.time()
print("COMBINATION 2")
combination2([], 0, R, 0)
print("SUM : ", g_comb2_sum)
print("CNT : ", g_comb2_cnt)
print("TIME : ", time.time() - time_before)

  
# COMBINATION 3
def combination3(comb_list, length, r, idx):
	global g_comb3_sum
	global g_comb3_cnt
	if length == r:
		g_comb3_cnt += 1
		for i in comb_list:
			g_comb3_sum += i
		return
	for i in range(idx, LEN_NUM):
		comb_list.append(numbers[i])
		combination3(comb_list, length + 1, r, i + 1)
		comb_list.pop()

time_before = time.time()
print("COMBINATION 3")
combination3([], 0, R, 0)
print("SUM : ", g_comb3_sum)
print("CNT : ", g_comb3_cnt)
print("TIME : ", time.time() - time_before)
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