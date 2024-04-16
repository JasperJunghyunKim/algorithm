#
# 24-03-18
# 첫 번째와 마지막이 순환되는 구조이므로, 첫 번째를 선택하는 경우와 마지막을 선택하는 경우를 구분해서 DP 실행
# 백준 평범한 배낭 문제랑 비슷
#

def solution(money):
    
    N = len(money)
    
    # DP1 : 첫 번째 집을 선택하는 경우(마지막은 선택하지 않음)
    dp1 = [0] * (N - 1)
    dp1[0] = money[0]
    dp1[1] = dp1[0]
    for i in range(2, N - 1):
        dp1[i] = max(dp1[i-1], money[i] + dp1[i-2])
     
    # DP2 : 마지막 집을 선택하는 경우(첫 번째는 선택하지 않음)
    dp2 = [0] * N
    dp2[0] = 0
    dp2[1] = money[1]
    for i in range(2, N):
        dp2[i] = max(dp2[i-1], money[i] + dp2[i-2])

    # DP1, DP2 각각의 마지막 결과를 비교
    return max(dp1[N - 2], dp2[N - 1])

if __name__ == "__main__":
    money = [1,2,3,1]
    result = solution(money)
    print(result)