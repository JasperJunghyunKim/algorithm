import sys
sys_input = sys.stdin.readline
N_NUMBERS = int(sys_input().strip())
numbers = list(map(int, sys_input().strip().split()))
N_PLUS, N_MINUS, N_MUL, N_DIV = map(int, sys_input().strip().split())

g_max = -float('inf')
g_min = float('inf')

def backtrack(value, n_plus, n_minus, n_mul, n_div, idx):
    global g_max, g_min
    if idx == N_NUMBERS:
        g_max = value if value > g_max else g_max
        g_min = value if value < g_min else g_min
        return
    
    if n_plus > 0:
        backtrack(value + numbers[idx], n_plus - 1, n_minus, n_mul, n_div, idx + 1)
    if n_minus > 0:
        backtrack(value - numbers[idx], n_plus, n_minus - 1, n_mul, n_div, idx + 1)
    if n_mul > 0:
        backtrack(value * numbers[idx], n_plus, n_minus, n_mul - 1, n_div, idx + 1)
    if n_div > 0:
        if value < 0 and numbers[idx] > 0:
            backtrack(-((-value) // numbers[idx]), n_plus, n_minus, n_mul, n_div - 1, idx + 1)
        else:
            backtrack(value // numbers[idx], n_plus, n_minus, n_mul, n_div - 1, idx + 1)
    



        
    
    
backtrack(numbers[0], N_PLUS, N_MINUS, N_MUL, N_DIV, 1)
print(g_max, g_min, sep="\n")
    