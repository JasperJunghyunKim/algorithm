import sys
sys_input = sys.stdin.readline
N = int(sys_input().strip())
synergy = [list(map(int, sys_input().strip().split())) for _ in range(N)]
min_gap_synergy = float('inf')

# 0 ~ N - 1
selected = [False for _ in range(N)]

def find_answer():
    global min_gap_synergy
    team_a = [i for i, v in enumerate(selected) if v == True]
    team_b = [i for i, v in enumerate(selected) if v == False]
    synergy_a = 0
    synergy_b = 0
    for a1 in team_a:
        for a2 in team_a:
            synergy_a += synergy[a1][a2]
    for b1 in team_b:
        for b2 in team_b:
            synergy_b += synergy[b1][b2]
    min_gap_synergy = abs(synergy_a - synergy_b) if abs(synergy_a - synergy_b) < min_gap_synergy else min_gap_synergy
    

def backtrack(n, idx):
    if n == N // 2:
        find_answer()
        return
    for i in range(idx, N):
        selected[i] = True
        backtrack(n + 1, i + 1)
        selected[i] = False
        
backtrack(0, 0)
print(min_gap_synergy)
