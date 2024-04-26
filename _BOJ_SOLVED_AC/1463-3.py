import sys

sys.setrecursionlimit(1_000_000)
N = int(input())
memo = [-1 for _ in range(N + 1)]


def dp(n):
    if memo[n] != -1: return memo[n]
    if n % 6 == 0:
        memo[n] = min(dp(n // 2), dp(n // 3), dp(n - 1)) + 1
    elif n % 2 == 0 and n % 3 != 0:
        memo[n] = min(dp(n // 2), dp(n - 1)) + 1
    elif n % 2 != 0 and n % 3 == 0:
        memo[n] = min(dp(n // 3), dp(n - 1)) + 1
    else:
        memo[n] = dp(n - 1) + 1
    return memo[n]


if N == 1:
    print(0)
elif N == 2:
    print(1)
elif N == 3:
    print(1)
elif N == 4:
    print(2)
else:
    memo[1] = 0
    memo[2] = 1
    memo[3] = 1
    memo[4] = 2
    # top down
    # print(dp(N))

    # bottom up
    for i in range(5, N + 1):
        if i % 6 == 0:
            memo[i] = min(memo[i//2], memo[i//3], memo[i-1]) + 1
        elif i % 2 == 0 and i % 3 != 0:
            memo[i] = min(dp(i // 2), dp(i - 1)) + 1
        elif i % 2 != 0 and i % 3 == 0:
            memo[i] = min(dp(i // 3), dp(i - 1)) + 1
        else:
            memo[i] = dp(i - 1) + 1
    print(memo[N])
