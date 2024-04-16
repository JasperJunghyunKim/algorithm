# ########################################
# # Bottom Up 1

# n = int(input().strip())
# tc = []
# for i in range(n):
#     tc.append(int(input().strip()))

# for i in tc:
#     num_cases = [0, 1, 2, 4]
#     for j in range(4, i + 1):
#         num_cases.append(num_cases[j-1] + num_cases[j-2] + num_cases[j-3])
#     print(num_cases[i])

# ########################################
# # Bottom Up 2

# n = int(input().strip())
# tc = []
# for i in range(n):
#     tc.append(int(input().strip()))

# for i in tc:
#     num_cases = [0, 1, 2, 4]
#     add_num_cases = num_cases.append
#     for j in range(4, i + 1):
#         add_num_cases(num_cases[j-1] + num_cases[j-2] + num_cases[j-3])
#         # num_cases.append(num_cases[j-1] + num_cases[j-2] + num_cases[j-3])
#     print(num_cases[i])

########################################
# Top Down
import sys
n = int(input().strip())
tc = []
for i in range(n):
    tc.append(int(input().strip()))
dp = {1:1, 2:2, 3:4}
def num_cases(n):
    if dp.get(n) == None:
        dp[n] = num_cases(n-1) + num_cases(n-2) + num_cases(n-3)
    return dp.get(n)
for i in tc:
    print(num_cases(i))