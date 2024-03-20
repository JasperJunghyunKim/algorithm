#
# 24-03-20
# 주식가격이 떨어질 때 까지를 측정하는 것 -> 문제가 이상함
#

from collections import deque
def solution(prices):
    N = len(prices)
    answer = []
    
    for i in range(N):
        for j in range(1, N - i):
            if prices[i+j] < prices[i]:
                answer.append(j)
                break
        else:
            answer.append(N - i - 1)
    
    return answer

print(solution([1, 2, 3, 2, 3]))