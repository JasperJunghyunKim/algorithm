#
# 24-03-19
# 블로그 보고 해결함
# 점화식 조건 : https://gurumee92.tistory.com/164
#

def solution(N, number):
    
    dp = dict()
    dp[1] = [N]
    dp[2] = [N * 11, N + N, N // N]
    for i in range(3, 9):
        dp[i] = []
        # 기본 꼴
        a = ""
        for _ in range(i):
            a += str(N)
        a = int(a)
        1 <= int(a) <= 32_000
        dp[i].append(a)
        
        # 조합(?)
        for j in range(1, i):
            list_a = dp[j]
            list_b = dp[i-j]
            for a in list_a:
                for b in list_b:
                    if 1 <= a + b <= 32_000 and a + b not in dp[i]:
                        dp[i].append(a + b)
                    if 1 <= a - b <= 32_000 and a - b not in dp[i]:
                        dp[i].append(a - b)
                    if 1 <= a * b <= 32_000 and a * b not in dp[i]:
                        dp[i].append(a * b)
                    if 1 <= a // b <= 32_000 and a // b not in dp[i]:
                        dp[i].append(a // b)
                    if 1 <= b - a <= 32_000 and b - a not in dp[i]:
                        dp[i].append(b - a)
                    if 1 <= b // a <= 32_000 and b // a not in dp[i]:
                        dp[i].append(b // a)
    
    # find number
    for key in dp.keys():
        for target in dp[key]:
            if number == target: 
                return key
    else:
        return -1