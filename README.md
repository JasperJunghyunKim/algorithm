
##### 24-03-19
- DFS 와 백트래킹
	- 여행경로
	- N Queen
	- N 과 M
* dict keys
* 집합 ... iter 종류 재확인
* https://medium.com/@chullino/if-name-main-%EC%9D%80-%EC%99%9C-%ED%95%84%EC%9A%94%ED%95%A0%EA%B9%8C-bc48cba7f720
* DP 시, bottom up, top down 적합 조건
* combination, permutation
* 


- 전역 참조가 불가하면 list[0] 인덱스를 사용하는 방법
- 최단거리는 BFS / 다익스트라 사용
	DFS(깊이 우선 탐색)를 사용하여 최단 거리 문제를 해결할 때 성능이 좋지 않은 주된 이유는, DFS가 모든 가능한 경로를 탐색하기 때문에 비효율적으로 많은 시간을 소모할 수 있기 때문입니다. 특히, 최단 거리를 찾는 문제의 경우에는 더욱 그렇습니다. 다음은 DFS 사용 시 성능이 좋지 않은 구체적인 이유들입니다:

1. **비효율적인 경로 탐색**: DFS는 한 방향으로 가능한 깊숙이 탐색을 진행한 후에야 다른 방향을 탐색합니다. 이 과정에서 최단 경로와는 크게 벗어난 긴 경로를 먼저 탐색할 수 있으며, 최단 경로가 아닌 많은 경로들을 불필요하게 탐색하게 됩니다.

2. **중복 탐색**: 특정 노드를 방문했을 때, 이 노드를 통해 도달할 수 있는 다른 노드들에 대한 탐색을 반복적으로 수행할 수 있습니다. 특히, 사이클이 있는 그래프에서는 무한 반복의 위험이 있습니다. 최단 거리 문제에서는 방문했던 노드를 또 다시 방문하는 것이 대부분 불필요하므로, 이러한 중복 탐색은 많은 시간 낭비를 야기합니다.

3. **최단 거리 보장 불가**: DFS는 모든 경로를 탐색하긴 하지만, 최초로 목적지에 도달했을 때의 경로가 반드시 최단 거리임을 보장하지 않습니다. 따라서, 모든 가능한 경로를 탐색한 후에야 최단 거리를 판별할 수 있으며, 이는 매우 비효율적입니다.

4. **자원 소모**: DFS는 재귀 호출을 많이 사용하게 되는데, 이는 호출 스택의 크기를 증가시키고, 결국 스택 오버플로를 일으킬 위험을 증가시킵니다. 또한, 많은 메모리를 소모할 수 있습니다.

	최단 거리 문제에서는 보통 BFS나 다익스트라 알고리즘 같은 다른 알고리즘이 훨씬 더 효율적입니다. BFS는 레벨 별로 탐색을 진행하기 때문에, 최초로 목적지에 도달했을 때의 경로가 최단 거리임을 보장합니다. 다익스트라 알고리즘은 가중치가 있는 그래프에서 최단 거리를 찾는데 사용됩니다.
* 


###### 23-03-18
* N QUEEN - 
* 

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