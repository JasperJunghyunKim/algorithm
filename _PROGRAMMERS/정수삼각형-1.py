#
# 24-03-19
# Bottom Up
#

def solution(triangle):
    
    # 초기값 (0 층) 설정
    dp = dict()
    dp[0] = [triangle[0][0]]
    height = len(triangle)
    
    # 1층부터 DP 순회 - Bottom Up
    for h in range(1, height):
        dp[h] = []
        for i, val in enumerate(triangle[h]):            
            # 첫번째 또는 마지막
            if i == 0:
                dp[h].append(dp[h-1][i] + val)
            elif i == len(triangle[h]) - 1: 
                dp[h].append(dp[h-1][i - 1] + val)
            # 사이
            else:
                dp[h].append(max(dp[h-1][i-1], dp[h-1][i]) + val)
                
    # 마지막층 중 최대값
    return max(dp[height - 1])

if __name__ == "__main__":
    triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    print(solution(triangle))