# # BottomUp - 시간초과
# import sys
# input = sys.stdin.readline
# n = int(input())

# fibonacci = [0] * 5
# fibonacci[0] = 0
# fibonacci[1] = 1
# fibonacci[2] = 1
# fibonacci[3] = 2

# for i in range(4, n+1):
#     fibonacci[i%5] = (fibonacci[(i-1)%5] + fibonacci[(i-2)%5])%1_000_000

# print(fibonacci[n%5]%1_000_000)

# BottomUp - PISANO PERIOD(피사노주기)
# 피사노 주기 : 피보나치 수를 K로 나눈 나머지는 항상 주기를 갖게된다는 원리
# 주기의 길이가 P(isano)일때, N 번째 피보나치 수를 M으로 나눈 나머지는 N%P 번째 피보나치수를 M 으로 나눈 나머지와 같음
# 나누려는 수가 M = 10^k (k>2) 일 때, 주기는 항상 15*10^(k-1)
# 예제에서 M = 10^6 이므로 주기(P)는 15*10^5

import sys
input = sys.stdin.readline
n = int(input())%(15*10**5)

fibonacci = [0] * 5
fibonacci[0] = 0
fibonacci[1] = 1
fibonacci[2] = 1
fibonacci[3] = 2

for i in range(4, n+1):
    fibonacci[i%5] = (fibonacci[(i-1)%5] + fibonacci[(i-2)%5])%1_000_000

print(fibonacci[n%5]%1_000_000)

