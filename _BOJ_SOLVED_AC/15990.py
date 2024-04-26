

########################################
# 23-12-14 (2)
# 아래 23-12-14 (1) 에서 초기 배열 할당을 수정했는데, 시간이 600ms 단축됨
import sys
sys_input = sys.stdin.readline

tc = int(sys_input())
dp = [[0,0,0,0] for _ in range(4)]
arr = []
dp[1] = [0,1,0,0]
dp[2] = [0,0,1,0]
dp[3] = [0,1,1,1]
for _ in range(tc):
    arr.append(int(sys_input()))
for i in range(4, max(arr)+1):
    dp.append([
        0, 
        (dp[i-1][2] + dp[i-1][3])%1_000_000_009,
        (dp[i-2][3] + dp[i-2][1])%1_000_000_009,
        (dp[i-3][1] + dp[i-3][2])%1_000_000_009])

for n in arr:
    print(sum(dp[n])%1_000_000_009)

########################################
# 23-12-14 (1)
# Bottom Up 시간초과는 아닌데 ... 시간이 오래 걸림
import sys
sys_input = sys.stdin.readline

tc = int(sys_input())
dp = [[0,0,0,0] for _ in range(1_000_001)]
arr = []
dp[1] = [0,1,0,0]
dp[2] = [0,0,1,0]
dp[3] = [0,1,1,1]
for _ in range(tc):
    arr.append(int(sys_input()))
for i in range(4, max(arr)+1):
    dp[i][1] = (dp[i-1][2] + dp[i-1][3])%1_000_000_009
    dp[i][2] = (dp[i-2][3] + dp[i-2][1])%1_000_000_009
    dp[i][3] = (dp[i-3][1] + dp[i-3][2])%1_000_000_009

for n in arr:
    print(sum(dp[n])%1_000_000_009)

# ########################################
# # Bottom Up - 1차 시기 통과
# from sys import stdin
# n = int(stdin.readline())
# tc = []

# for i in range(n):
#     tc.append(int(stdin.readline()))

# one = [0,1,0,1]
# two = [0,0,1,1]
# three = [0,0,0,1]

# for i in range(4, max(tc) + 1):
#     one.append((two[i-1] + three[i-1])%1_000_000_009)
#     two.append((three[i-2] + one[i-2])%1_000_000_009)
#     three.append((one[i-3] + two[i-3])%1_000_000_009)

# for i in tc:
#     print((one[i] + two[i] + three[i])%1_000_000_009)

# ########################################
# # Bottom Up - 2차 시기 통과
# from sys import stdin
# n = int(stdin.readline())
# tc = []

# for i in range(n):
#     tc.append(int(stdin.readline()))


# dp = [[0,0,0], [1,0,0], [0,1,0], [1,1,1]]


# for i in range(4, max(tc) + 1):
#     dp.append([(dp[i-1][1] + dp[i-1][2])%1_000_000_009, (dp[i-2][2] + dp[i-2][0])%1_000_000_009, (dp[i-3][0] + dp[i-3][1])%1_000_000_009])

# for i in tc:
#     print((sum(dp[i]))%1_000_000_009)

# # ########################################
# # # Top Down
# # from sys import stdin
# # from sys import setrecursionlimit
# # setrecursionlimit(10**5)
# # n = int(stdin.readline())
# # tc = []ㄱ
# # for i in range(n):
# #     tc.append(int(stdin.readline()))

# # one = {0:0, 1:1, 2:0, 3:1}
# # two = {0:0, 1:0, 2:1, 3:1}
# # three = {0:0, 1:0, 2:0, 3:1}

# # def find_case(n, is_123):
# #     if is_123 == 1:
# #         if one.get(n) == None:
# #             one[n] = (find_case(n-1, 2) + find_case(n-1, 3))%1_000_000_009
# #         return one.get(n)
# #     elif is_123 == 2:
# #         if two.get(n) == None:
# #             two[n] = (find_case(n-2, 3) + find_case(n-2, 1))%1_000_000_009
# #         return two.get(n)
# #     elif is_123 == 3:
# #         if three.get(n) == None:
# #             three[n] = (find_case(n-3, 1) + find_case(n-3, 2))%1_000_000_009
# #         return three.get(n)
    
# # for i in tc:
# #     print(find_case(i, 1) + find_case(i, 2) + find_case(i, 3))