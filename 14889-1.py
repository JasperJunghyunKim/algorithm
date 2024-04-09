import sys
sys_input = sys.stdin.readline

N = int(sys_input().strip())
power_map = [list(map(int, sys_input().strip().split())) for _ in range(N)]
min_val = float('inf')


def get_team_power(team):
    power = 0
    for i in range(N//2):
        for j in range(i + 1, N//2):
            power += power_map[team[i]][team[j]]
            power += power_map[team[j]][team[i]]
    return power
    
def comb(new_team, size_team, idx):
    global min_val
    if size_team == N // 2:
        team_a = [i for i in range(N) if new_team[i] == True]
        team_b = [i for i in range(N) if new_team[i] == False]
        gap = abs(get_team_power(team_a) - get_team_power(team_b))
        min_val = gap if gap < min_val else min_val
        return
    
    for k in range(idx, N):
        new_team[k] = True
        comb(new_team, size_team + 1, k + 1)
        new_team[k] = False

        
comb([False for _ in range(N)], 0, 0)
print(min_val)
