#
import sys
sys_input = sys.stdin.readline
g_count  = 0

def factorial(n):
    if n == 0: return 1
    if n == 1: return 1
    return n * factorial(n-1)
def combination(cnt, n, r, idx):
    global g_count
    if cnt == r:
        g_count += 1
        return
    for i in range(idx, n):
        combination(cnt + 1, n, r, i + 1)

for _ in range(int(sys_input().strip())):
    A, B = map(int, sys_input().strip().split())
    # g_count = 0
    # combination(0, B, A, 0)
    # print(g_count)
    print(int(factorial(B) / (factorial(B-A) * factorial(A))))



