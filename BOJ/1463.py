########################################
# 23-12-14 (2)
n = int(input().strip())
dp = [-1] * 1_000_001
dp[1] = 0
for i in range(2, n+1):
    if (i % 3 == 0 and i % 2 == 0):
        dp[i] = min(dp[i//3], dp[i//2], dp[i-1]) + 1
    elif (i % 3 == 0):
        dp[i] = min(dp[i//3], dp[i-1]) + 1
    elif (i % 2 == 0):
        dp[i] = min(dp[i//2], dp[i-1]) + 1
    else:
        dp[i] = dp[i-1] + 1
print(dp[n])
    
########################################
# 23-12-14 (1)
# 시간초과 -> 3 2 로 모두 나눠지는 조건에서 findOne(a-1) 지우면 해결됨 ... 아마도 나눌 수 있다면 무조건 작게 나누는게 제일 빨라서 그런듯

import sys
sys.setrecursionlimit(10**6)
n = int(input().strip())
dp = [-1] * 1_000_001
dp[1] = 0

def findOne(a):
    if (dp[a] >= 0): return dp[a]
        
    if (a % 3 == 0 and a % 2 == 0):
        dp[a] = min(findOne(a//3), findOne(a//2), findOne(a-1)) + 1
    elif (a % 3 == 0):
        dp[a] = min(findOne(a//3), findOne(a-1)) + 1
    elif (a % 2 == 0):
        dp[a] = min(findOne(a//2), findOne(a-1)) + 1
    else:
        dp[a] = findOne(a-1) + 1
    return dp[a]

print(findOne(n))
        

########################################
# # T3 : Top Down
# # RecursionError 가 뜨는데, n % 3 == 0 and n % 2 == 0 조건에서 make_one(n-1) 을 제거하니 해결됨. 이유는 모름.

# import sys
# sys.setrecursionlimit(10000)
# input = sys.stdin.readline
# n = int(input().strip())

# dp = {1:0, 2:1, 3:1,}

# def make_one(n):
#     if dp.get(n) != None:
#         return dp.get(n)
#     else:
#         if n % 3 == 0 and n % 2 == 0:
#             dp[n] = min(make_one(n//3), make_one(n//2), make_one(n-1)) + 1
#         elif n % 3 == 0:
#             dp[n] = min(make_one(n//3), make_one(n-1)) + 1
#         elif n % 2 == 0:
#             dp[n] = min(make_one(n//2), make_one(n-1)) + 1
#         else:
#             dp[n] = make_one(n-1) + 1
#         return dp.get(n)

# print(make_one(n))

# ########################################
# # T4 : Bottom Up
# import sys
# input = sys.stdin.readline
# n = int(input().strip())

# dp = [0, 0, 1, 1]
# for i in range(4, n+1):
#     if i % 3 == 0 and i % 2 == 0:
#         dp.append(min(dp[i//3], dp[i//2], dp[i-1]) + 1)
#     elif i % 3 == 0:
#         dp.append(min(dp[i//3], dp[i-1]) + 1)
#     elif i % 2 == 0:
#         dp.append(min(dp[i//2], dp[i-1]) + 1)
#     else:
#         dp.append(dp[i-1] + 1)

# print(dp[n])