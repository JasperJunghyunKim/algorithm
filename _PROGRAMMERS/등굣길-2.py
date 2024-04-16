#
# 24-03-19
#
def solution(m, n, puddles):
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    dp[1][1] = 1
    
    for row in range(1, m + 1):
        for col in range(1, n + 1):
            if row == 1 and col == 1:
                continue
            if [row, col] in puddles: 
                continue
            dp[row][col] = (dp[row - 1][col] + dp[row][col -1]) % 1_000_000_007
    
    return dp[m][n]

if __name__ == "__main__":
    m = 4
    n = 3
    puddles = [[2, 2]]
    # puddles = [[1, 1], [2, 1], [1, 2], [3, 1]]
    result = solution(m,n,puddles)
    print(result)