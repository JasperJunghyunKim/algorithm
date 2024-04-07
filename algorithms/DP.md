### 개념

* Dynamic Programming (동적 계획법)
* 복잡한 문제를 더 작은 하위 문제로 나누어 해결하는 알고리즘 설계 기법
* 중복된 형태의 하위 문제의 결과를 저장하고 재활용 함으로써, 계산 효율성을 향상시키는 것이 핵심

**DP 기법을 적용시킬 수 있는 조건**
1. 중복되는 부분 문제
   문제를 나누고 그 문제의 결과 값을 재활용해서 전체 답을 구함
   따라서 동일한 작은 문제들이 반복하여 나타나는 경우에 사용 가능
2. 중복되는 부분 문제
   큰 문제의 최적 해결책이 그 문제의 부분 문제들의 최적 해결책으로부터 구성될  수 있음을 의미
   즉, 전체 문제의 해가 부분 문제의 해에서 유도될 수 있을 때 사용 가능



---
### 구현

1. DP 배열을 정의한다. 
   이때 DP 는 다차원 배열이 될 있다.
   * 예1) DP\[i\] : i 번째까지 실행했을 때의 최대값
   * 예2) DP\[i\]\[w\] 번째까지 고려했을 때, 최대 무게 w 를 넘지 않는 범위 내에서 얻을 수 있는 최대 가치
1. DP 배열의 점화식을 찾는다. 2, 3차원 배열이될 수도 있으며, 배열 간 서로 영향을 줄 수도 있음
2. Bottom Up 또는 Top Down 중 적절한 방식으로 구현한다.

### 구현_Bottom Up (Tabulation 방식)

* 작은 문제부터 차례대로 해결하면서 그 결과를 테이블에 저장하고, 이 테이블 값을 이용하여 점차 큰 문제의 해결책을 구성해 나감
* 일반적으로 반복문을 이용하여 구현

### 구현_Top Down (Memoization 방식)

* 큰 문제를 작은 부분 문제로 나누어 해결하는 방식
* 이를 위해 재귀함수를 사용하여 문제를 작은 부분 문제로 쪼개고, 중복되는 계산을 피하기 위해 Memoization 을 활용

### 구현 비교 - Top Down vs Bottom Up

* 둘 다 공통적으로 한 번 계산된 값을 저장하는 특징이 있음

**Bottom Up** 
* 반복문을 순회하며 작은 문제의 결과를 테이블에 저장하므로, 코드가 일반적으로 더 직관적임
* 반복문만 사용하므로 재귀 호출의 오버헤드와 스택 오버플로우의 위험이 없음
* 그러나, 전체 문제 공간을 미리 정의해야되며 모든 하위 문제를 해결해야만 최종 문제를 해결할 수 있음
	* 그러니 전체 공간을 정의하는 것은, '나머지' 를 활용하는 방식으로 테이블 길이를 단축시킬 수 있음

**Top Down**
* 필요한 하위 문제만을 해결하기 때문에, 불필요한 계산을 줄일 수 있음
* 모든 하위 문제의 해를 저장해야되므로, 메모리 사용량이 증가할 수 있음
* 재귀 호출에 따른 오버헤드 및 깊은 재귀로 인한 스택 오버플로우


---
### 유형

* DP 는 점화식을 잘 정의하는 것이 핵심
* 점화식을 찾는 것이 어려우므로 주의
* 또한 점화식마다 인덱스의 범위 제한을 정해야되는 경우도 있음
* 대부분의 문제에서 공통적으로 점화식 DP를 아래와 같이 정의했음
	**순서가 정해져 있는 경우**
	1. dp\[i\] 는 i 번째를 선택할 때의 최적해
	2. dp\[i\] 는 i 번째를 반드시 선택할 경우의 최적해
	3. dp\[i\]\[k\] 는 k 라는 제한된 범위에 대해, i 번째 아이템을 선택할 경우의 최적해
	
	**순서가 정해져 있지 않은 경우**
	1. 

1. 피보나치 수
2. [평범한 배낭 1](https://www.acmicpc.net/problem/12865)
	
	* [0-1 Knapsack Problem](Knapsack.md)
	* 제한된 무게 내에서 최대의 가치를 만들 수 있는 아이템들을 선택하는 문제 
		$$dp[i][capa] = max(dp[i-1][capa], v_i + dp[i-1][capa - w_i]$$
	* dp\[i\]\[capa\] 는 제한된 무게가 capa 일 때, i 번째 아이템을 선택할 때의 최대 가치
	* dp\[i-1\]\[capa\]
	  i 번째 아이템을 선택하지 않는 경우를 의미
	  즉, 동일한 제한 무게 capa 에 대하여 i-1 째 아이템을 선택하는 최대 가치와 같음
	* v_i + dp\[i-1\]\[capa - w_i\]
	  i 번째 아이템을 선택하는 경우를 의미
	  i 를 선택하므로 v 만큼 더하고, 제한 무게는 선택한 w 만큼 뺀 값으로 줄어듦

3. [평범한 배낭 2](https://www.acmicpc.net/problem/12920)
	
	* 
4. [퇴사](https://www.acmicpc.net/problem/14501)
	
	* [0-1 Knapsack Problem](Knapsack.md)
	* 제한된 시간 내에서 최대의 가치를 만들 수 있는 미팅을 선택하는 문제
	* 단, [평범한 배낭 1](https://www.acmicpc.net/problem/12865) 문제와 달리, Day(index)가 증가하면서, 제한되는 시간이 자동으로 1 씩 추가로 차감됨
		$$dp[i][d] = max(dp[i-1][d+1], p_i + dp[i-1][d+1-t_i])$$
	* 제한된 날짜가 d 일 때, i 째 날에 미팅을 진행할 경우의 최대 가치
	* dp\[i-1\]\[d+1\]
	  i 째 날에 미팅을 진행하지 않을 경우를 의미
	  즉, i - 1 째 날의 최적해와 같음
	  단, 이 문제에선 하루 전으로 당기게 되면, 제한된 날짜는 자동으로 하루가 많아지므로 d + 1 이 됨  

5. [포도주 시식](https://www.acmicpc.net/problem/2156)
	$$dp[i] = max(wine[i] + wine[i-1] + dp[i-3], wine[i] + dp[i-2], dp[i-1])$$
	* dp\[i\] 는 i 번째 포도주를 시직할 때의 최대량
	* wine\[i\] + wine\[i-1\] + dp\[i-3\]
	  i, i-1 에서는 마시고, i-2 는 마시지 않는 경우
	  즉, i-2 는 마시지 않으므로, i-3 의 최대량을 고려하는 것과 동일
	* wine\[i\] + dp\[i-2\]
	  i 에서는 마시고, i-1 은 마시지 않는 경우
	  즉, i-1 은 마시지 않으므로, i-2 의 최대량을 고려하는 것과 동일
	* dp\[i-1\]
	  i 에서 와인을 마시지 않는 경우를 의미, 즉, i-1 째 칸까지의 최대량과 동일
	* 어느 위치에서 마시지 않는지를 기준으로 조건을 정리하는 것이 핵심
	  i 를 마시지 않으면, i-1 까지의 최대량과 같음
	
5. [계단오르기](https://www.acmicpc.net/problem/2579)
	$$dp[i] = max(step[i] + step[i-1] + dp[i-3], step[i] + dp[i-2])$$
	* dp\[i\] 는 i 째 계단을 무조건 밟았을 때의 최대값
	* step\[i\] + step\[i-1\] + dp\[i-3\]
	  i - 2 째를 밟지 않는 경우가 포함되어 있음
	* step\[i\] + dp\[i-2\]
	  i - 1 째를 밟지 않는 경우가 포함되어 있음
	* [이 코드](../BOJ_SOLVED_AC/2579-2.py)를 보면 i 째 계단을 밟지 않는 경우를 고려한 DP 배열, i 째 계단을 밟는 경우를 고려한 DP_MUST 배열을 둘 다 정의했는데, 결국 풀어보니 DP_MUST 만 사용함
	  즉, DP 배열을 잘 정의하는 것이 매우 중요


6. 길이 N 배열 여러개가 서로 영향을 주는 점화식 예) [RGB 거리](https://www.acmicpc.net/problem/1149)
7. 최장 증가 부분 수열(Longest Increasing Subsequence, LIS)
8. 최장 공통 부분 수열(Longest Common Subsequence, LCS)


---
### ⚠️ 주의

### 참고

### 정리중