#
# 24-03-19
# 5번정도 처음부터 시도했으나 실패 (예제는 맞는데, 제출 시 틀림)
#

def solution(m, n, puddles):
    dp = [[(0,0) for _ in range(n)] for _ in range(m)]
    dp[0][0] = (0,1)
    puddles = [[col, row] for [row, col] in puddles]
    
    for row in range(m):
        for col in range(n):
            if [row, col] in puddles or (row == 0 and col == 0): 
                continue
            
            prev_left = [row, col - 1]
            prev_upper = [row - 1, col]
            if row - 1 < 0:
                if prev_left in puddles: 
                    continue
                else:
                    dp[row][col] = (dp[row][col - 1][0] + 1, dp[row][col - 1][1] % 1_000_000_007)
            elif col - 1 < 0:
                if prev_upper in puddles:
                    continue
                else:
                    dp[row][col] = (dp[row - 1][col][0] + 1, dp[row - 1][col][1] % 1_000_000_007)
            else:
                if prev_upper in puddles and prev_left in puddles:
                    continue
                elif prev_upper in puddles:
                    dp[row][col] = (dp[row][col - 1][0] + 1, dp[row][col - 1][1] % 1_000_000_007)
                elif prev_left in puddles:
                    dp[row][col] = (dp[row - 1][col][0] + 1, dp[row - 1][col][1] % 1_000_000_007)
                else:
                    dp[row][col] = (dp[row][col - 1][0] + 1, (dp[row - 1][col][1] + dp[row][col - 1][1]) % 1_000_000_007)
            
    # print(*dp, sep="\n")
    return dp[m-1][n-1][1]

if __name__ == "__main__":
    m = 4
    n = 3
    # puddles = [[2, 2]]
    puddles = [[1, 1], [2, 1], [1, 2], [3, 1]]
    result = solution(m,n,puddles)
    print(result)