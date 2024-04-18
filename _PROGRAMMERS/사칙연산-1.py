# dp[a][b] : a 번째 숫자 ~ b 번째 숫자에 대한 최대값 (a, b 는 숫자를 의미하는 인덱스)
#

def solution(arr):
    LEN_ARR = len(arr)
    NUM_OPERANDS = len(arr) // 2 + 1
    NUM_OPERATORS = len(arr) // 2
    max_dp = [[-float('inf')] * LEN_ARR for _ in range(LEN_ARR)]
    min_dp = [[float('inf')] * LEN_ARR for _ in range(LEN_ARR)]

    #
    for i in range(0, LEN_ARR, 2):
        max_dp[i][i] = int(arr[i])
        min_dp[i][i] = int(arr[i])

    # a, b 사이의 간격
    for dist in range(2, LEN_ARR, 2): # 0, 2, 4, 6, 8
        for a in range(0,LEN_ARR - dist,2): #
            b = a + dist
            for i in range(a, b - 1, 2): # a ~ b - 2
                # dp[a][b] = dp[a][i] (i+1) dp[i+2][b]
                if arr[i + 1] == "+":
                    max_value = max_dp[a][i] + max_dp[i + 2][b]
                    min_value = min_dp[a][i] + min_dp[i + 2][b]
                elif arr[i + 1] == "-":
                    max_value = max_dp[a][i] - min_dp[i + 2][b]
                    min_value = min_dp[a][i] - max_dp[i + 2][b]
                max_dp[a][b] = max(max_dp[a][b], max_value)
                min_dp[a][b] = min(min_dp[a][b], min_value)

    return max_dp[0][len(arr)-1]

# arr = ["1", "-", "3", "+", "5", "-", "8"]
# print(solution(arr))