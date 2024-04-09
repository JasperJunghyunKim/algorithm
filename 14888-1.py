#
# BackTracking, BruteForce
# 

import sys
sys_input = sys.stdin.readline
import itertools
N_NUMBERS = int(sys_input().strip())
numbers = list(map(int, sys_input().strip().split()))
N_PLUS, N_MINUS, N_MUL, N_DIV = map(int, sys_input().strip().split())
PLUS, MINUS, MUL, DIV = 1, 2, 3, 4
operator = [PLUS for _ in range(N_PLUS)] + [MINUS for _ in range(N_MINUS)] + [MUL for _ in range(N_MUL)] + [DIV for _ in range(N_DIV)]

max_val = -float('inf')
min_val = float('inf')

def find_min_max(p):
    global max_val
    global min_val
    val = numbers[0]
    for i in range(N_NUMBERS - 1):
        if p[i] == PLUS:
            val = val + numbers[i+1]
        elif p[i] == MINUS:
            val = val - numbers[i+1]
        elif p[i] == MUL:
            val = val * numbers[i+1]
        elif p[i] == DIV:
            if val < 0 and numbers[i+1] > 0:
                val = -((-val) // numbers[i+1])
            else:
                val = val // numbers[i+1]
    max_val = val if val > max_val else max_val
    min_val = val if val < min_val else min_val

visited = [False for _ in range(len(operator))]
def perm(new_arr, len_arr, r):
    if len_arr == r:
        find_min_max(new_arr)
        return
    for i in range(len(operator)):
        if not visited[i]:
            visited[i] = True
            new_arr[len_arr] = operator[i]
            len_arr += 1
            perm(new_arr, len_arr, r)
            len_arr -= 1
            visited[i] = False

# perm([0 for _ in range(len(operator))], 0,len(operator))

p_list = list(itertools.permutations(operator, len(operator)))
for p in p_list:
    find_min_max(p)





print(max_val, min_val, sep="\n")
        

    