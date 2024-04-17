import sys
sys_input = sys.stdin.readline

N = int(sys_input().strip())
cheerleaders = [[float('inf')] * (N + 1) for _ in range(N + 1)]
for r in range(1, N + 1):
    cheerleaders[r][r] = 0
while True:
    c1, c2 = map(int, sys_input().strip().split())
    if c1 == -1 and c2 == -1:
        break
    cheerleaders[c1][c2] = 1
    cheerleaders[c2][c1] = 1

def floyd_warshall():
    for stopover in range(1, N + 1):
        for c1 in range(1, N + 1):
            for c2 in range(1, N + 1):
                cheerleaders[c1][c2] = min(cheerleaders[c1][c2], cheerleaders[c1][stopover] + cheerleaders[stopover][c2])

floyd_warshall()

chairman_score = float('inf')
chairman_candidates = []
for i in range(1, N + 1):
    score = max(cheerleaders[i][1:])
    if score < chairman_score:
        chairman_score = score
        chairman_candidates = [i]
    elif score == chairman_score:
        chairman_candidates.append(i)

print(chairman_score, len(chairman_candidates))
print(*chairman_candidates)