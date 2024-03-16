
###### 문제
- [BOJ 14500](https://www.acmicpc.net/problem/14500)
	- DFS 재귀 전후 visited check 조건
- [BOK]()
- 


###### 23-03-16
* 참조형 vs (?) / 그리고 전역 범위
* swap 한번에
* combination, perm
* max(2D graph)
* BFS, DFS 꼴 복습
* 'meetings.sort(key=lambda x: (x[1], x[0]))'
* 

###### 23-03-15
- BFS, DFS
- Divide Conquer
- 자료구조 불변

## 자료구조
- 스택
- 덱
- 


## DP
- 재귀 (top down)
- 메모이제이션 점화식 (bottom up)
- 

## 사용법
- 각 컬렉션 ... 등의 추가, 제거 방법


## 코드

```python

import sys
input = sys.stdin.readline

n = int(input())

```


### 익힐것
* 슬라이싱
* 키 밸류 같이 출력하는 거
* sys.stdin.readline / input 차이
* sys.stdout.write / print 차이
* strip
* append 시 메모리 재할당이 발생하므로 메모리를 효율적으로 사용하지 못함
* enumerate


## 참고사항
* visited 체크를 꼭 is in 으로 확인하지 말고, index + boolean 적용해서 시간 단축
* 